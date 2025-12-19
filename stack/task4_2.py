from stack.task4 import Stack

# Задание 4
# задача 5
# Валидация баланса строки с круглыми скобками
# время O(n) память O(n)
def validate_staples(staples):
    stack = Stack()

    for i in staples:
        if i == '(':
            stack.push(i)
            continue

        stap = stack.pop()

        if stap is None:
            return False

    return stack.size() == 0

# Задание 4
# задача 6
# Валидация баланса строки с разными скобками
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

# Задание 4
# задача 7, 8
# Добавление в стек функции для возвращения текущего минимального элемента
# и функции среднего значения всех элементов
# время для обеих добавленных функций O(1)
class StackWithMinAvg:
    def __init__(self):
        self.stack = []
        self.count = 0
        self.min_stack = Stack()
        self.sum = 0

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.count == 0:
            return None

        deleted_element = self.stack.pop(0)
        self.count -= 1

        last_min = self.min_stack.peek()

        if last_min == deleted_element:
            self.min_stack.pop()

        self.sum -= deleted_element

        return deleted_element

    def push(self, value):
        self.stack.insert(0, value)
        self.count += 1

        last_min = self.min_stack.peek()

        if last_min >= value:
            self.min_stack.push(value)

        self.sum += value

    def peek(self):
        return self.stack[0] if self.count > 0 else None

    def get_min_element(self):
        return self.min_stack.peek()

    def get_avg_element(self):
        return int(self.sum / self.count)

# Задание 4
# задача 9
# Вычисление выражения с постфиксной записью
# время O(n) память O(n)
def calculate_with_postfix(postfix):
    start_stack = Stack()
    numbers_stack = Stack()
    calculate_type = {
        '+': lambda x, y: int(x) + int(y),
        '-': lambda x, y: int(x) - int(y),
        '*': lambda x, y: int(x) * int(y),
        '/': lambda x, y: int(x) / int(y),
    }

    postf_list = postfix.split(' ')
    postf_list.reverse()
    for i in postf_list:
        start_stack.push(i)

    while start_stack.size() > 0:
        sym = start_stack.pop()

        if sym.isdigit():
            numbers_stack.push(sym)
            continue

        first_number = numbers_stack.pop()

        if sym == '=':
            return first_number

        second_number = numbers_stack.pop()
        numbers_stack.push(calculate_type.get(sym)(first_number, second_number))

    return numbers_stack.pop()

# Рефлексия задач второго задания:
# Метод, который "переворачивает" связный список.
# Задание выполнено неправильно, т.к я хотел воспользоваться только методами, которые предлагает сам
# список, без нод и просто достал все ноды с удалением и их последующим добавлением в другом порядке.

# Проверка, имеются ли циклы внутри списка.
# Задание выполнено аналогично приведенному решению.

# Сортировка списка.
# задача была решена быстрой сортировкой и изначально собирала все ноды в массив

# Слияние списков.
# Задание выполнено аналогично приведенному решению.

# Dummy.
# Задание пропущено, решение добавлено ниже


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class DummyNode(Node):
    def __init__(self):
        super().__init__(None)

class LinkedList2:
    def __init__(self):
        dummy = DummyNode()
        self.head = dummy
        self.tail = dummy
        dummy.next = dummy
        dummy.prev = dummy
        self.count = 0

    def add_in_tail(self, item):
        cur_prev = self.tail.prev
        self.tail.prev = item
        cur_prev.next = item

        item.next = self.tail
        item.prev = cur_prev

        self.count += 1

    def find(self, val):
        node = self.head.next

        while not isinstance(node, DummyNode):
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result_nodes = []
        node = self.head.next

        while not isinstance(node, DummyNode):
            if node.value == val:
                result_nodes.append(node)
            node = node.next

        return result_nodes

    def delete(self, val, all=False):
        node = self.head.next
        continue_delete = True

        while not isinstance(node, DummyNode) and continue_delete:
            if node.value == val:
                self.__remove_node(node)
                continue_delete = all
            node = node.next

    def __remove_node(self, node):
        self.count -= 1
        current_prev = node.prev
        current_next = node.next

        current_prev.next = current_next
        current_next.prev = current_prev

    def clean(self):
        dummy = self.head
        dummy.next = dummy
        dummy.prev = dummy
        self.count = 0

    def len(self):
        return self.count # здесь будет ваш код

    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.add_in_tail(newNode)
            return

        self.count += 1
        current_next = afterNode.next

        afterNode.next = newNode
        newNode.prev = afterNode

        newNode.next = current_next
        current_next.prev = newNode

    def add_in_head(self, newNode):
        self.count += 1
        current_head = self.head.next

        self.head.next = newNode
        newNode.next = current_head
        current_head.prev = newNode

