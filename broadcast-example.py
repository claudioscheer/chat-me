# -*- coding: utf-8 -*-
import socket
import threading
import uuid
import time

name = "Claudio"
broadcast = "255.255.255.255"
port = 6777
local_id = uuid.uuid4()
announce_interval = 3


def announcer():
    socket_announcer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_announcer.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    announce_message = "%s:%s" % (local_id.hex, name)

    while 1:
        socket_announcer.sendto(announce_message, (broadcast, port))
        time.sleep(announce_interval)

def broadcastListener():
    socket_broadcast = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_broadcast.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_broadcast.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    socket_broadcast.bind(("0.0.0.0", port))
    
    while 1:
        data = socket_broadcast.recvfrom(1024)
        if not data:
            break
        print data

if __name__ == "__main__":
    thread_broadcast_listener = threading.Thread(target = broadcastListener)
    thread_announcer = threading.Thread(target = announcer)
    
    thread_broadcast_listener.start()
    thread_announcer.start()
