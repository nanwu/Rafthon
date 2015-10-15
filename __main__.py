import socket
import argparse
import sys

class Server():
    
    def __init__(self, port, cluster_id=0):
        self.port = port
        self.host = '127.0.0.1'
        self.cluster_id = cluster_id

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)   # optional backlog param since 3.5

        while True:
            try:
                c, addr = self.socket.accept()
                print("got connection from", addr)
                c.send(b'Thank you for connecting') 
                c.close()
            except KeyboardInterrupt:
                print('Bye')
                self.socket.close()
                sys.exit()

def main():
    server = Server(8081)
    server.run()

if __name__ == '__main__':
    main()
