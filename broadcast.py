import socket
import threading
import time

class BroadCastProxy:
    
    def __init__(self, port):
        self.port = port
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

            self.socket.bind(('', 50000))
        except socket.error, message:
            pass


    def run(self):
        t_recv = threading.Thread(target=self.read)
        t_recv.start()

        t_send = threading.Thread(target=self.write)
        t_send.start()

    def read(self):
        while True:
            data, addr = self.socket.recvfrom(self.port)
            print(str(data))

    def write(self):
        while True:
            time.sleep(2)
            self.socket.sendto(b'I am alive!\n', ('<broadcast>', self.port))

proxy = BroadCastProxy(50000)
proxy.run()
