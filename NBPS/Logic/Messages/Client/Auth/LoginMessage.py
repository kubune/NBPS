from NBPS.Server.Datastream.Reader import Reader
from NBPS.Logic.Handlers.Helpers import Helpers
from NBPS.Logic.Messages.Server.Auth.LoginOkMessage import LoginOkMessage
from NBPS.Logic.Messages.Server.Auth.LoginFailedMessage import LoginFailedMessage
from NBPS.Logic.Messages.Server.Home.OwnHomeDataMessage import OwnHomeDataMessage
from NBPS.Logic.Messages.Server.Alliance.MyAllianceMessage import MyAllianceMessage
from NBPS.Logic.Messages.Server.Alliance.AllianceStreamMessage import AllianceStreamMessage
from NBPS.Logic.Messages.Server.Home.LobbyInfoMessage import LobbyInfoMessage


class LoginMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.helpers = Helpers()

    def decode(self):

        self.account_id    = self.readLong()
        self.account_token = self.readString()
        self.player.game_major    = self.readInt()
        self.player.game_minor    = self.readInt()
        self.player.game_build    = self.readInt()

        self.fingerprint_sha = self.readString()


    def process(self, db):

        if self.player.maintenance:
            self.player.err_code = 10
            LoginFailedMessage(self.client, self.player, '').send()

        if self.fingerprint_sha != self.player.patch_sha and self.player.patch:
            self.player.err_code = 7
            LoginFailedMessage(self.client, self.player, "").send()

        if self.account_id == 0:
            self.player.ID = db.get_player_count() + 1
            self.player.token = self.helpers.randomToken()
            db.create_player_account(self.player.ID, self.player.token)

        else:
            self.player.ID = self.account_id
            self.player.token = self.account_token
            player_data = db.load_player_account(self.player.ID, self.player.token)
            if player_data:
                Helpers.load_account(self, player_data)
                if self.player.club_id != 0:
                	club_data = db.load_club(self.player.club_id)
                	Helpers.load_club(self, club_data)
            else:
                db.create_player_account(self.player.ID, self.player.token)


        LoginOkMessage(self.client, self.player, self.player.ID, self.player.token).send()
        OwnHomeDataMessage(self.client, self.player).send()
        LobbyInfoMessage(self.client, self.player, 0).send()
        if self.player.club_id != 0:
            club_data = db.load_club(self.player.club_id)
            MyAllianceMessage(self.client, self.player, club_data).send()
            AllianceStreamMessage(self.client, self.player, club_data['Messages']).send()
