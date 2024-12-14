

class Fragment:
    def __init__(self, fragmentStr):
        self.fullStr = fragmentStr.strip()
        self.tail = int(self.fullStr[:2])
        self.body = int(self.fullStr[2:4])
        self.head = int(self.fullStr[4:])

    def __str__(self):
        return(f"{self.tail:0>2d}{self.body:0>2d}{self.head:0>2d}")

    