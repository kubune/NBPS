from NBPS.Server.Datastream.Reader import Reader
from NBPS.Logic.Messages.Server.Team.TeamMessage import TeamMessage


class TeamCreateMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.map_slot  = self.readVInt()
        self.map_id    = self.readVInt()
        self.room_type = self.readVInt()

    def process(self, db):
        TeamMessage(self.client, self.player, self.room_type).send()