import uuid
import json
from modules import Sockets, config, Election


sockets = Sockets.Sockets()
election = Election.Election()
local_uuid = uuid.uuid4()


def main():
    election.init_election(sockets, local_uuid.int)
    #sockets.socket_sender.sendto(json.dumps(vote), (config.ip, config.port))


if __name__ == "__main__":
    main()
