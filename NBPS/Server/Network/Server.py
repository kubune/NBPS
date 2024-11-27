import json
import socket
from NBPS.Logic.Handlers.Helpers import Helpers
from NBPS.Server.Network.ClientThread import ClientThread
from NBPS.Logic.Handlers.Debugger import _print, Colors, Styles

def _(colors, *args):
    text = ""
    for arg in args:
        text += arg + " "
    _print(text, colors[0], colors[1])

class Server:
    clients_count = 0

    def __init__(self, ip: str, port: int):
        self.config = json.loads(open('NBPS/Configuration/config.json', 'r').read())
        self.server = socket.socket()
        self.port = port
        self.ip = ip

    def start(self):
        self.server.bind((self.ip, self.port))


        _([Colors.BLUE, Colors.CYAN], f'[DEBUG] Server started! Listening on {self.ip}:{self.port}')

        if self.config.get("Maintenance"):
            _([Colors.RED, Colors.YELLOW],f'[WARNING] Maintenance is enabled! Disable it using a command or in Configuration/config.json')
        while True:
            self.server.listen()
            client, address = self.server.accept()

            _([Colors.WHITE, Colors.GRAY],f'[DEBUG] Client connected! IP: {address[0]}')

            ClientThread(client, address).start()

            Helpers.connected_clients['ClientsCount'] += 1