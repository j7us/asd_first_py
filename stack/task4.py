class Stack:
    def __init__(self):
        self.stack = []
        self.count = 0

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.count == 0:
            return None

        deleted_element = self.stack.pop(0)
        self.count -= 1
        return deleted_element

    def push(self, value):
        self.stack.insert(0, value)
        self.count += 1

    def peek(self):
        return self.stack[0] if self.count > 0 else None

# Мера сложности pop и push O(1) при добавлении в конец списка
# 3 задание - цикл может вывести в какой-то момент None, т.к каждый pop удаляет по одному элементу
# 4 задание - мера сложности при добавлении в начало может быть O(n) т.к приходится сдвигать элементы

