


class Lock:
    """ Lamport Lock """

    def __init__(self):
        self.term = 0

    def incre(self):
        self.term += 1 
