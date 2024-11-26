from NBPS.Server.Datastream.Reader import Reader
from NBPS.Logic.Messages.Server.Team.TeamMessage import TeamMessage

class TeamToggleSettingsMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.use_gadget = self.readBool()
        self.room_type = 0

    def process(self, db):
        TeamMessage(self.client, self.player, self.room_type).send()