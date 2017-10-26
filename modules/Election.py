import threading
import json
import socket
from modules.config import ip, port


class Election:
    def __init__(self):
        pass

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
        while 1:
            try:
                data = sockets.socket_receiver.recv(1024)
                vote_received = json.loads(data)
                if vote_received["voto_distribuidor"] == 0:
                    print vote_received
                else:
                    sockets.send_message(self.get_vote(
                        local_uuid, vote_received.voto_instancia), ip)
                    break
            except socket.timeout:
                print "No vote received."
        sockets.socket_receiver.settimeout(None)
