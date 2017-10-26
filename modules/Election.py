import threading
import json
import socket
from modules.config import ip, port


class Election:
    def __init__(self):
        self.server_elected = None
        self.server_uuid = None

    def get_vote(self, local_uuid, vote_uuid):
        return {
            "remetente": local_uuid,
            "tipo": 0,
            "voto_instancia": vote_uuid,
            "voto_distribuidor": 0,
        }

    def init_election(self, sockets, local_uuid):
        receive_votes_thread = threading.Thread(
            target=self.receive_votes, args=(sockets, local_uuid))
        receive_votes_thread.start()

        receive_votes_thread.join()

    def receive_votes(self, sockets, local_uuid):
        sockets.socket_receiver.settimeout(5)
        sockets.send_message(self.get_vote(local_uuid, local_uuid), ip)
        server_already_selected = 0
        while 1:
            try:
                data, socket_address = sockets.socket_receiver.recvfrom(1024)
                vote_received = json.loads(data)
                voto_instancia = vote_received["voto_instancia"]
                if voto_instancia == local_uuid:
                    continue
                if vote_received["voto_distribuidor"] == 0:
                    if voto_instancia < local_uuid:
                        sockets.send_message(self.get_vote(
                            local_uuid, local_uuid), ip)
                    else:
                        sockets.send_message(self.get_vote(
                            local_uuid, voto_instancia), ip)
                server_already_selected = 1
                self.server_elected = socket_address
                self.server_uuid = voto_instancia
            except socket.timeout:
                if server_already_selected:
                    break
                else:
                    print "No vote received."
        sockets.socket_receiver.settimeout(None)
        print self.server_elected
        print self.server_uuid
