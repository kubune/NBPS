import time
import json
from threading import *
from NBPS.Logic.Structures.Player import Player
from NBPS.Logic.Structures.Device import Device
from NBPS.Logic.Handlers.Helpers import Helpers
from NBPS.Logic.Messages.LogicLaserMessageFactory import packets
from NBPS.Logic.Messages.Server.Auth.LoginFailedMessage import LoginFailedMessage
from NBPS.Server.Database.DBManager import DB
from NBPS.Logic.Handlers.Debugger import _print, Colors, Styles

def _(colors, *args):
    text = ""
    for arg in args:
        text += arg + " "
    _print(text, colors[0], colors[1])



class ClientThread(Thread):
    def __init__(self, client, address):
        super().__init__()
        self.client = client
        self.address = address
        self.db = DB
        self.config = json.loads(open('NBPS/Configuration/config.json', 'r').read())
        self.device = Device(self.client)
        self.player = Player(self.device)
        self.player.IP = address[0]


    def recvall(self, length: int):
        data = b''

        while len(data) < length:
            s = self.client.recv(length)

            if not s:
                _([Colors.RED, Colors.YELLOW], f"[ERROR] while receiving data!")
                break

            data += s
        return data



    def run(self):
        self.db = self.db()
        try:
            last_packet = time.time()
            while True:
                header = self.client.recv(7)

                if len(header) > 0:

                    self.banned = json.loads(open('NBPS/Configuration/banned.json', "r").read())

                    last_packet = time.time()

                    # Packet Info
                    packet_id = int.from_bytes(header[:2], 'big')
                    packet_length = int.from_bytes(header[2:5], 'big')
                    packet_data = self.recvall(packet_length)

                    if self.address[0] in self.banned.keys():
                        self.player.err_code = 11
                        LoginFailedMessage(self.client, self.player, f'Account banned!\nReason: {self.banned[self.player.IP]}').send()


                    if packet_id in packets:
                        packet_name = packets[packet_id].__name__
                        _([Colors.GREEN, Colors.CYAN],f'[CLIENT] PacketID: {packet_id}, Name: {packet_name} Length: {packet_length}')

                        message = packets[packet_id](self.client, self.player, packet_data)
                        message.decode()
                        message.process(self.db)

                        if packet_id == 10101:
                            Helpers.connected_clients["Clients"][str(self.player.ID)] = {"SocketInfo": self.client}
                            self.db.update_player_account(self.player.token, 'IP', self.player.IP)


                    else:
                        _([Colors.GRAY, Colors.PINK],f'[CLIENT] Unhandled Packet! ID: {packet_id}, Length: {packet_length}')

                if time.time() - last_packet > 10:
                    _([Colors.WHITE, Colors.GRAY],f"[DEBUG] Client disconnected! IP: {self.address[0]}")
                    self.client.close()
                    self.db.close()
                    _([Colors.WHITE, Colors.GRAY],f"[DEBUG] Client disconnected! IP: {self.address[0]}")
                    Helpers.connected_clients['ClientsCount'] -= 1
                    break


        except ConnectionAbortedError:
            _([Colors.WHITE, Colors.GRAY],f"[DEBUG] Client disconnected! IP: {self.address[0]}")
            self.client.close()
            self.db.close()
            Helpers.connected_clients['ClientsCount'] -= 1
        except ConnectionResetError:
            _([Colors.WHITE, Colors.GRAY],f"[DEBUG] Client disconnected! IP: {self.address[0]}")
            self.client.close()
            self.db.close()
            Helpers.connected_clients['ClientsCount'] -= 1
        except TimeoutError:
            _([Colors.WHITE, Colors.GRAY],f"[DEBUG] Client disconnected! IP: {self.address[0]}")
            self.client.close()
            self.db.close()
            Helpers.connected_clients['ClientsCount'] -= 1