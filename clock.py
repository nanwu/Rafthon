from threading import Lock


class Clock:

    def __init__(self):
        self.term = 0
        self.mutex = Lock()

    def incre(self):
        with self.mutex:
            self.term += 1 
            return self.term

    def forward(self, other):
        with self.mutex:
            self.term = other

