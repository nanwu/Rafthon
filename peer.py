import random
import time
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

from rafthon import status
from rafthon.clock import Clock
from rafthon.rpc import RPCServer
import threading

TIMEOUT_MAX = 300
TIMEOUT_MIN = 150
timestamp_now = lambda: int(round(time.time() * 1000))

class Peer:
    
    def __init__(self, addr, port):
        self.leader = None
        self.rpc_server = RPCServer(addr, port, peer=self)
        self.status = status.FOLLOWER
        self.term = Clock()

    def append_entry(self, entry):
        pass

    def request_vote(self, (addr, port), term):
        if self.status == status.LEADER or term < self.term:
            return False

        if term == self.term and self.status == status.CANDIDATE:
            return False

        if term > self.term:
            

    def run(self):
        self.last_event_timestamp = timestamp_now()
        self.election_timout = random.randint(TIMEOUT_MIN, TIMEOUT_MAX)
        while :
            if timestamp_now() - self.last_event_timestamp >= self.election_timout:
                self.clock.incre()
                self.status = status.CANDIDATE
                # issue request_vote in parralle
                for neighbor in self.neighbors:

        



def main():

if __name__ == "__main__":
    main()
