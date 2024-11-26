from NBPS.Server.Datastream.Writer import Writer
from NBPS.Logic.Handlers.Helpers import Helpers
from NBPS.Logic.Commands.Server.Home.LogicChangeAvatarNameCommand import LogicChangeAvatarNameCommand
from NBPS.Logic.Commands.Server.Home.LogicSetSupportedCreatorCommand import LogicSetSupportedCreatorCommand
from NBPS.Logic.Commands.Server.Delivery.LogicGiveDeliveryItemsCommand import LogicGiveDeliveryItemsCommand

class AvailableServerCommandMessage(Writer):

    def __init__(self, client, player, commandID):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.commandID = commandID

    def encode(self):

        commands = {
            201: LogicChangeAvatarNameCommand,
            203: LogicGiveDeliveryItemsCommand,
            215: LogicSetSupportedCreatorCommand
        }

        if self.commandID in commands:

            self.writeVInt(self.commandID)
            commands[self.commandID].encode(self)
        else:
            print(f"{Helpers.yellow}[SERVER] Cannot create command! ID: {self.commandID}")