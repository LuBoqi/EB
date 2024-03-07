import time


class Message:
    def __init__(self, sender):
        self.time = None
        self.content = None
        self.receiver = None
        self.sender = sender
        self.spliter = '\r\n'

    def en_code(self, sender, receiver, strs):
        msg = self.spliter + self.spliter
        tmp = [sender, receiver, strs, get_time_string()]
        for item in tmp:
            msg = msg + str(item) + self.spliter
        return msg.encode()

    def de_code(self, msg):
        msg = [data for data in msg.split(self.spliter) if data]
        self.sender = msg[0]
        self.receiver = msg[1]
        self.content = msg[2]
        self.time = msg[3]


def get_time_string():
    # 获取当前时间戳
    current_time = time.time()
    # 使用time.localtime()将时间戳转换为本地时间的结构化表示
    local_time = time.localtime(current_time)
    # 获取年、月、日、时、分、秒
    year = local_time.tm_year
    month = local_time.tm_mon
    day = local_time.tm_mday
    hour = local_time.tm_hour
    minute = local_time.tm_min
    second = local_time.tm_sec
    # 将时间信息拼接成一个字符串
    time_string = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(year, month, day, hour, minute, second)
    return time_string
