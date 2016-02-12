from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

from rafthon.status import FOLLOWER, CANDIDATE, LEADER
from rafthon.lock import Lock
from rafthon.rpc import RPCServer
import threading

class Peer:
    
    def __init__(self, addr, port):
        self.leader = None
        self.rpc_server = RPCServer(addr, port, peer=self)

    def append_entry(self, entry):
        pass

    def request_vote(self):
        pass


def main():

if __name__ == "__main__":
    main()
