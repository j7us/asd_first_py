from deque.task6 import Deque
from stack.task4 import Stack


# Задание 6
# задача 7.3
# Проверка строки на палиндром
# время O(n) память O(n)
def is_palindrome(text):
    deq = Deque()
    for i in text:
        deq.addTail(i)

    for i in range(int(len(text) / 2)):
        t = deq.removeTail()
        f = deq.removeFront()

        if t != f:
            return False

    return True

# Задание 6
# задача 7.4
# Нахождение минимума в очереди
# время O(1)
class DequeWithMin:
    def __init__(self):
        self.buffer = []
        self.min_buffer = []

    def addFront(self, item):
        self.buffer.append(item)

        cur_min_f = self.min_buffer[-1] if len(self.min_buffer) > 0 else item

        if cur_min_f >= item:
            self.min_buffer.append(item)

    def addTail(self, item):
        self.buffer.insert(0, item)

        cur_min_f = self.min_buffer[0] if len(self.min_buffer) > 0 else item

        if cur_min_f >= item:
            self.min_buffer.insert(0, item)

    def removeFront(self):
        deleted = self.buffer.pop() if len(self.buffer) > 0 else None

        if deleted is not None and deleted == self.min_buffer[-1]:
            self.min_buffer.pop()

        return deleted

    def removeTail(self):
        deleted = self.buffer.pop(0) if len(self.buffer) > 0 else None

        if deleted is not None and deleted == self.min_buffer[0]:
            self.min_buffer.pop(0)

        return deleted

    def size(self):
        return len(self.buffer)

    def min(self):
        return min(self.min_buffer[0], self.min_buffer[-1]) if len(self.min_buffer) > 0 else None


# Задание 6
# задача 7.5
# Реализация очереди чрез динамически массив
# реализовано в основном задании


# Задание 6
# задача 7.6
# Баланс скобок
# время O(n) память O(n)
def validate_staples_with_different_type(staples):
    stap_types = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = Stack()

    for i in staples:
        if stap_types.get(i) is None:
            stack.push(i)
            continue

        stap = stack.pop()

        if stap is None or stap != stap_types.get(i):
            return False

    return stack.size() == 0


# Рефлексия задач задания 4:
# Задачи 5 и 6 "валидация скобок" выполнены в соответствии с предложенным решением
# Задача 7 "Текущий минимальный элемент в стеке" выполнена в соответствии с предложенным решением
# Задача 8 "Среднее значение всех элементов в стеке" выполнена в соответствии с предложенным решением
# Задача 9 "Постфиксная запись выражения" выполнена в варианте использования словаря и лямбда-функций

