import os
import json
import requests

Files = "NBPS/Server/Files"
changelog = """
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
