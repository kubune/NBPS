from NBPS.Server.Datastream.Writer import Writer

class ShutdownStartedMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20161
        self.player = player

    def encode(self):
        self.writeVInt(0)

