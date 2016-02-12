from xmlrpc.server import SimpleXMLRPCServer


class RPCServer:
    
    def __init__(self, addr, port, peer):
	self.peer = peer
        self._server = SimpleXMLRPCServer((addr, port))
        self._server.register_function(self.peer.append_entry, 'append_entry')
        self._server.register_function(self.peer.request_vote, 'request_vote')

    def start(self):
        server_thread = threading.Thread(target=self._server.serve_forever)
        server_thread.daemn = True
        server_thread.start()

    def close(self):
        self._server.shutdown()
        self._server.server_close()

