import json
import socket
from NBPS.Logic.Handlers.Helpers import Helpers
from NBPS.Server.Network.ClientThread import ClientThread

def _(*args):
    for arg in args:
        print(arg, end=' ')
    print()

class Server:
    clients_count = 0

    def __init__(self, ip: str, port: int):
        self.config = json.loads(open('NBPS/Configuration/config.json', 'r').read())
        self.server = socket.socket()
        self.port = port
        self.ip = ip

    def start(self):
        self.server.bind((self.ip, self.port))

        _(f'{Helpers.cyan}[DEBUG] Server started! Listening on {self.ip}:{self.port}')

        while True:
            self.server.listen()
            client, address = self.server.accept()

            _(f'{Helpers.cyan}[DEBUG] Client connected! IP: {address[0]}')

            ClientThread(client, address).start()

            Helpers.connected_clients['ClientsCount'] += 1