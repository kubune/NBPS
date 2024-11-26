from NBPS.Logic.Logic.ClientHome import LogicClientHome
from NBPS.Logic.Logic.ClientAvatar import LogicClientAvatar
from NBPS.Server.Datastream.Writer import Writer
from datetime import datetime
from NBPS.Server.Database.DBManager import DB
from NBPS.Logic.Handlers.Helpers import Helpers

class OwnHomeDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.client = client
        self.player = player
        self.time_stamp = int(datetime.timestamp(datetime.now()))

    def encode(self):
        DataManager = DB()
        if self.player.token != None:
        	player_data = DataManager.load_player_account(self.player.ID, self.player.token)
        	Helpers.load_account(self, player_data)
        DataManager.close()
        LogicClientHome.encode(self)
        LogicClientAvatar.encode(self)
        self.writeVInt(self.time_stamp)