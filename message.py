import time


class Message:
    def __init__(self, sender):
        self.time = None
        self.content = None
        self.receiver = None
        self.sender = sender

    def encode(self, receiver, strs):
        tmp = [self.sender, receiver, strs, time.time()]
        msg = ''
        for item in tmp:
            msg = msg + str(item) + ' '
        return msg

    def decode(self, msg):
        self.receiver = msg[1]
        self.sender = msg[0]
        self.content = msg[2]
        self.time = msg[3]
