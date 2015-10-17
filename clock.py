
from threading import Lock

class LClock:
    """ Lamport's logical clock
    
    """

    def init(self):
        self.term = 0
        self.mutex = Lock()

    def incre(self):
        with self.mutex:
            self.term += 1
            return self.term

    def adjust(self, other_term):
        with self.mutex:
            if other_term > self.term:
                self.term += 1


        
