from NBPS.Server.Datastream.Writer import Writer
from NBPS.Logic.Handlers.ServerConfig import ServerConfig

class LobbyInfoMessage(Writer):
    def __init__(self, client, player, count):
        super().__init__(client)
        self.id = 23457
        self.player = player
        self.count = count
        self.serverConfig = ServerConfig()
        serverConfigData = self.serverConfig.load()
        self.message = ""
        if serverConfigData.get('showLobbyInfo') == False:
            self.showLobbyInfo = False
        else:
            self.showLobbyInfo = True
        if serverConfigData.get('customLobbyInfo').get('enabled') == True:
            self.customLobbyInfo = True
            for line in serverConfigData.get('customLobbyInfo').get('lines'):
                self.message += line + "\n"
        else:
            self.customLobbyInfo = False

        self.newlines = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

    def encode(self):
        if self.showLobbyInfo:
            self.writeVInt(self.count)
            self.writeString(f"NBPS: {self.player.game_major}.{self.player.game_build}.{self.player.game_minor}\n"
                             f"Rewritten by @kubune\n"
                             f"Server core by @8hacc\n\n"
                             f"{self.message}"
                             f"{self.newlines}"
                             )
        else:
            self.writeVInt(self.count)
            self.writeString(f"{self.newlines}")

        self.writeVInt(0)  # array
        for x in range(0):
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)