class Proxy:
    pass

proxy = Proxy()

def request_vote(host, term):
    if not proxy.has_voted(term):
        proxy.vote_for(host)

