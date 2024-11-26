from NBPS.Server.Datastream.Reader import Reader
from NBPS.Logic.Messages.Server.Auth.KeepAliveOkMessage import KeepAliveOkMessage
from NBPS.Logic.Messages.Server.Home.LobbyInfoMessage import LobbyInfoMessage
from NBPS.Logic.Handlers.Helpers import Helpers

class KeepAliveMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self, db):
        KeepAliveOkMessage(self.client, self.player).send()
        LobbyInfoMessage(self.client, self.player, Helpers.connected_clients['ClientsCount']).send()
