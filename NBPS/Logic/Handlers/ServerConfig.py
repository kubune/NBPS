import os
import json

configuration = "NBPS/Configuration"

default_config = {
    "showLobbyInfo": True,
    "skipTutorial": True,

    "customLobbyInfo": {
        "enabled": True,
        "lines": [
            "Brawl Nova is the best!",
            "My own private server!"
        ]
    }
}

class ServerConfig:
    def __init__(self):
        if os.path.exists(f"{configuration}/server.json"):
            self.config = json.loads(open(f"{configuration}/server.json", "r").read())
        else:
            with open(f"{configuration}/server.json", "w") as server:
                json.dump(default_config, server)

            self.config = default_config

    def load(self):
        return self.config