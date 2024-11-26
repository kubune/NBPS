import os
import json

from NBPS.Logic.Utils.TagUtils import tagToId
from NBPS.Server.Database.DBManager import DB
import traceback

def handle_command(command: str):
    arguments: list = command.split(" ")

    if arguments[0] == "ban":
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
    elif arguments[0] == "unban":
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

    else:
        print(f"Unknown command: {arguments[0]}")

