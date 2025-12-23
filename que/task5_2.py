from que.task5 import Queue
from stack.task4 import Stack

# Задание 5
# задача 3
# Вращение очереди на несколько элементов
# время O(n) память O(1)
def queue_rotation(queue: Queue, rotation_count):
    length = queue.size()

    if length == 0 or rotation_count == 0:
        return

    for i in range(rotation_count):
        el = queue.dequeue()
        queue.enqueue(el)

# Задание 5
# задача 4
# Очередь с двумя стеками
# enqueue - время O(1), dequeue - O(n)
class StacksQueue:
    def __init__(self):
        self.stack = Stack()
        self.reverse_stack = Stack()

    def enqueue(self, item):
        self.stack.push(item)

    def dequeue(self):
        return None if self.stack.size() == 0 and self.reverse_stack.size() == 0 else self.__find_last()

    def __find_last(self):
        if self.reverse_stack.size() == 0:
            self.__reverse()

        return self.reverse_stack.pop()

    def __reverse(self):
        cur_stack_len = self.stack.size()

        for i in range(cur_stack_len):
            self.reverse_stack.push(self.stack.pop())

    def size(self):
        return self.stack.size() + self.reverse_stack.size()


# Задание 5
# задача 5
# Очередь в обратном порядке
# время O(n) память O(n)
def reverse_queue(queue: Queue):
    if queue.size() == 0:
        return

    stack = Stack()

    for i in range(queue.size()):
        stack.push(queue.dequeue())

    for i in range(stack.size()):
        queue.enqueue(stack.pop())

# Задание 5
# задача 5
# Очередь в обратном порядке
# enqueue - время O(n), dequeue - O(1)
class FixArrayQueue:
    def __init__(self, capacity):
        self.buffer = []
        self.capacity = capacity
        self.count = 0

    def enqueue(self, item):
        if self.count >= self.capacity:
            raise Exception('Queue is full')

        self.buffer.insert(0, item)
        self.count += 1

    def dequeue(self):
        if len(self.buffer) < 0:
            return None

        self.count -= 1
        return self.buffer.pop()

    def size(self):
        return self.count

# Рефлексия задач задания 3:
# задание 6
# При выполнении удаления амортизационные добавляются 3, как и при добавлении,
# а при реаллокации списывается по формуле 2 ** int(math.log2(new_capacity))

# задание 7
# задание было выполнено корректно

