import json
import traceback
import time
from operator import truediv

from NBPS.Logic.Structures.Device import Device
from NBPS.Logic.Structures.Player import Player
from NBPS.Logic.Utils.TagUtils import tagToId
from NBPS.Server.Database.DBManager import DB
from NBPS.Logic.Handlers.Helpers import Helpers

from NBPS.Logic.Messages.Server.Auth.LoginFailedMessage import LoginFailedMessage
from NBPS.Logic.Messages.Server.Maintenance.ShutdownStartedMessage import ShutdownStartedMessage


def handle_command(command: str):
    arguments: list = command.split(" ")

    if arguments[0] == "ban":
        ban(arguments)
    elif arguments[0] == "unban":
        unban(arguments)
    elif arguments[0] == 'maintenance':
        maintenance(arguments)
    else:
        print(f"Unknown command: {arguments[0]}")

class maintenance():
    def __init__(self, arguments):
        try:
            if len(arguments) > 1:
                if arguments[1] == "off":
                    config = json.loads(open("NBPS/Configuration/config.json", "r").read())
                    config['Maintenance'] = False
                    json.dump(config, open("NBPS/Configuration/config.json", "w"), indent=4)
                    print("/maintenance: Turned off maintenance.")

        except:
            print(traceback.format_exc())
            print("/maintenance: Unknown error!")
            return
        try:
            config = json.loads(open("NBPS/Configuration/config.json", "r").read())
            allclients = Helpers.connected_clients
            self.database = DB()
            self.helpers = Helpers()
            clients = []
            players = []
            for client in list(allclients['Clients'].values()):
                self.device = Device(client)
                self.player = Player(self.device)
                player_data = self.database.get_player_data_by_ip(client['SocketInfo'].getpeername()[0])
                player = Helpers.load_account(self, player_data)
                ShutdownStartedMessage(client['SocketInfo'], player).send()
                clients.append(client['SocketInfo'])
                players.append(self.player)

            print("/maintenance: Sent Message!")
            config['Maintenance'] = True
            json.dump(config, open("NBPS/Configuration/config.json", "w"), indent=4)

            time.sleep(5.0)
            for i, client in enumerate(clients):
                player = players[i]
                player.err_code = 1
                player.maintenance = True

                LoginFailedMessage(client, player, 'Maintenance Started').send()
                client.close()
            print("/maintenance: Started maintenance!")
        except:
            print(traceback.format_exc())
            print("/maintenance: Unknown error!")
            return

def unban(arguments):
    try:
        if 2 > len(arguments):
            print("/unban: No tag specified!")
            return
        _, ID = tagToId(arguments[1])
        data = DB().load_player_account_by_id(ID)
        if data is None:
            print("/unban: Tag not found!")
            return
        ip = data.get("IP")
        banned: dict = json.loads(open("NBPS/Configuration/banned.json", "r").read())
        banned.pop(ip)
        json.dump(banned, open("NBPS/Configuration/banned.json", "w"))
        print(f"/unban: Unbanned {ip}")

    except:
        print(traceback.format_exc())
        print("/unban: Unknown error!")
        return

def ban(arguments):
    try:
        if 2 > len(arguments):
            print("/ban: No tag specified!")
            return
        _, ID = tagToId(arguments[1])
        data = DB().load_player_account_by_id(ID)
        if data is None:
            print("/ban: Tag not found!")
            return
        ip = data.get("IP")
        if 3 <= len(arguments):
            reason = ""
            for chunk in arguments[2:]:
                reason += chunk + " "
        else:
            reason = "No reason specified"

        banned = json.loads(open("NBPS/Configuration/banned.json", "r").read())
        with open("NBPS/Configuration/banned.json", "w") as ban:
            banned[ip] = reason
            json.dump(banned, ban)

        print(f"/ban: Banned {ip}, Reason: {reason}")

    except:
        print(traceback.format_exc())
        print("/ban: Unknown error!")
        return
