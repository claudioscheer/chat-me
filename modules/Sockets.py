import socket
import json
from modules.config import port


class Sockets:
    def __init__(self):
        self.create_socket_receiver()
        self.create_sockets_sender()

    def create_sockets_sender(self):
        self.socket_sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket_sender.setsockopt(
            socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def create_socket_receiver(self):
        self.socket_receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket_receiver.setsockopt(
            socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket_receiver.setsockopt(
            socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.socket_receiver.bind(("0.0.0.0", port))

    def send_message(self, _object, ip):
        object_json = json.dumps(_object)
        for i in range(3):
            self.socket_sender.sendto(object_json, (ip, port))
