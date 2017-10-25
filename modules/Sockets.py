from config import port
import socket
import json

class Sockets:
    def __init__(self):
        self.createSocketReceiver()
        self.createSocketSender()

    def createSocketSender(self):
        self.socket_sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket_sender.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def createSocketReceiver(self):
        self.socket_receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket_receiver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket_receiver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.socket_receiver.bind(("0.0.0.0", port))

    def sendMessage(self, _object, ip):
        object_json = json.dumps?!?jedi=0, (_object)?!? (param data, *_*param flags*_*, param address) ?!?jedi?!?
        self.socket_sender.sendto(object_json, (ip, port))
