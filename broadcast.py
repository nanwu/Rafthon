import socket
import threading
import time

class BroadCastServer:
    
    def __init__(self):
        self.recv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.recv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.recv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        self.send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.send_socket = socket.socket(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def run(self):
        self.read()
        self.write()

    def read(self):

    def 
    
while True:
    time.sleep(1000)
    s.sendto(b'I am alive!', ('255.255.255.255', 50000))
