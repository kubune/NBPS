import os
import json
import requests

versionCode = 1

versionCodeFromGithub = requests.get("https://raw.githubusercontent.com/kubune/NBPS/refs/heads/master/NBPS/Server/Extra/versionCode.txt")
if versionCodeFromGithub.status_code == 200:
    if versionCode < int(versionCodeFromGithub.text):
        print("A new version is available on github: https://github.com/kubune/NBPS")

Files = "NBPS/Server/Files"

changelog = """

    Changelog:
    
    1.1
    - Added command handler. Commands available now are: ban, unban.
    To show the command menu click "/"
    - Added version codes. If there'll be a new version on GitHub. You will get a notification.
    - Added reasons to bans.
    - Added server.json in Configuration. You can edit some stuff in it.
    - Some fixes

"""
changelog1_0 = """
    Changelog:
    
    1.0
    First version
    - Added new IDs support. Which means you'll get tags like #2PP etc.
    - Changed the structure of the project.
    
    """

class Changelog:
    def loadStates(self):
        try:
            if os.path.exists(f"{Files}/States.json"):
                with open(f"{Files}/States.json", "r") as States:
                    StatesData = json.load(States)
            else:
                with open(f"{Files}/States.json", "w") as States:
                    json_data = {
                        "SeenChangelog": False
                    }
                    json.dump(json_data, States)
                    StatesData = json_data

            return StatesData
        except:
            return {}

    def changeValue(self, key, value):
        data = self.loadStates()
        data[key] = value
        try:
            with open(f"{Files}/States.json", "w") as States:
                json.dump(data, States)
        except:
            pass

    def showChangelog(self):
        data = self.loadStates()
        state_SeenChangelog = data.get('SeenChangelog', False)
        if not state_SeenChangelog:
            print(changelog)
            self.changeValue('SeenChangelog', True)
        else:
            pass
