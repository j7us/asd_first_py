class Queue:
    def __init__(self):
        self.buffer = []

    def enqueue(self, item):
        self.buffer.insert(0, item)

    def dequeue(self):
        return self.buffer.pop() if len(self.buffer) > 0 else None

    def size(self):
        return len(self.buffer)

# enqueue - время O(n), dequeue - O(1)

