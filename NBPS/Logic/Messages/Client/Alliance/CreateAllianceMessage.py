from NBPS.Server.Datastream.Reader import Reader
from NBPS.Logic.Handlers.Helpers import Helpers
from NBPS.Logic.Messages.Server.Alliance.MyAllianceMessage import MyAllianceMessage
from NBPS.Logic.Messages.Server.Alliance.AllianceResponseMessage import AllianceResponseMessage
from NBPS.Logic.Messages.Server.Alliance.AllianceDataMessage import AllianceDataMessage


class CreateAllianceMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.club_name            = self.readString()
        self.club_desc            = self.readString()
        self.club_badge           = self.readDataReference()[1]
        self.club_region          = self.readDataReference()[1]
        self.club_type            = self.readVInt()
        self.club_req_trophies    = self.readVInt()
        self.club_family_friendly = self.readVInt()

    def process(self, db):
        data = {
            "Name": self.club_name,
            "Description": self.club_desc,
            "Region": self.club_region,
            "BadgeID": self.club_badge,
            "Type": self.club_type,
            "Trophies": self.player.trophies,
            "RequiredTrophies": self.club_req_trophies,
            "FamilyFriendly": self.club_family_friendly,
            "Members": [
                {
                 'Name': self.player.name,
                 'ID': self.player.ID,
                 'Role': 2,
                 'Trophies': self.player.trophies,
                 'ProfileIcon': self.player.profile_icon,
                 'NameColor': self.player.name_color
                 }
            ],
            "Messages": []
        }

        self.player.club_id = db.get_clubs_count() + 1
        self.player.club_role = 2

        db.create_club(self.player.club_id, data)
        db.update_player_account(self.player.token, 'ClubID', self.player.club_id)
        db.update_player_account(self.player.token, 'ClubRole', self.player.club_role)

        club_data = db.load_club(self.player.club_id)

        MyAllianceMessage(self.client, self.player, club_data).send()
        AllianceResponseMessage(self.client, self.player, 20).send()
        AllianceDataMessage(self.client, self.player, club_data).send()

