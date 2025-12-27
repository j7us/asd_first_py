class Deque:
    def __init__(self):
        self.buffer = []

    def addFront(self, item):
        self.buffer.append(item)

    def addTail(self, item):
        self.buffer.insert(0, item)

    def removeFront(self):
        return self.buffer.pop() if len(self.buffer) > 0 else None

    def removeTail(self):
        return self.buffer.pop(0) if len(self.buffer) > 0 else None

    def size(self):
        return len(self.buffer)

