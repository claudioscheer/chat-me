import uuid
import json
from modules import Sockets, config

sockets = Sockets()
local_uuid = uuid.uuid4()


def main():
    vote = {
        "remetente": local_uuid.int,
        "tipo": 0,
        "voto_instancia": local_uuid.int,
        "voto_distribuidor": 0,
    }

    sockets.socket_sender.sendto(json.dumps(vote), (config.ip, config.port))

if __name__ == "__main__":
    main()
