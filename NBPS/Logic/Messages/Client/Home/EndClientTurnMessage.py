from NBPS.Server.Datastream.Reader import Reader
from NBPS.Logic.Handlers.Helpers import Helpers
from NBPS.Logic.Commands.LogicCommandManager import commands
from NBPS.Logic.Handlers.Debugger import _print, Colors, Styles

def _(colors, *args):
    text = ""
    for arg in args:
        text += arg + " "
    _print(text, colors[0], colors[1])
    
class EndClientTurnMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.player = player

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.tick = self.readVInt()
        if self.tick != 0:
            self.commandID = self.readVInt()


    def process(self, db):
        if self.tick != 0:
            if self.commandID in commands:
                command = commands[self.commandID]
                try:
                    command.decode(self)
                    command.process(self, db)
                except AttributeError:
                    command(self.client, self.player).send() # Exception for OutOfSyncMessage
            else:
                _([Colors.Cyan, Colors.Gray],f'[CLIENT] Unhandled Command! ID: {self.commandID}')
