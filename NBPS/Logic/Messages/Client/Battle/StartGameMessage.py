from NBPS.Server.Datastream.Reader import Reader
from NBPS.Logic.Messages.Server.Team.TeamMessage import TeamMessage
from NBPS.Logic.Messages.Server.Battle.MatchMakingCancelledMessage import MatchMakingCancelledMessage
from NBPS.Logic.Logic.Home.LogicEventData import LogicEventData

class StartGameMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.map_slot = self.readVInt()


    def process(self, db):
        self.player.map_id = LogicEventData.events[self.map_slot - 1]['ID']

        MatchMakingCancelledMessage(self.client, self.player).send()
        TeamMessage(self.client, self.player).send()