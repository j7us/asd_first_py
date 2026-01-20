from ordered.task7_2 import OrderedListWithIndex, NodeWithIndex

# Задание 9
# задача 5
# Cловарь с использованием упорядоченного списка
# добавление происходит за O(n) поиск и удаление за O(log n)
class Bucket:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    def __cmp__(self, other):
        return -1 if self.key < other.key else 1 if self.key > other.key else 0


class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = OrderedListWithIndex(True)

    def is_key(self, key):
        ind = self.slots.find_index(Bucket(key))
        return ind >= 0

    def put(self, key, value):
        buc = Bucket(key, value)
        self.slots.add(buc)

    def get(self, key):
        res = self.slots.find(Bucket(key))
        return res.value if res else None

# Задание 9
# задача 6
# Cловарь с ключами битовыми строками
# добавление происходит за O(n) поиск и удаление за O(log n)
class BitNativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.count = 0
        self.step = 1

    def hash_fun(self, key):
        ind = hash(key) % self.size
        return ind * -1 if ind < 0 else ind

    def seek_slot(self, value, find_value_only=False):
        ind = self.hash_fun(value)
        ind_value = self.slots[ind]

        if (not find_value_only and (ind_value is None or ind_value ^ value == 0)) or (find_value_only and ind_value is not None and ind_value ^ value == 0):
            return ind

        return self.__find_slot_from_current(ind, find_value_only)

    def __find_slot_from_current(self, ind, value, find_value_only=False):
        slot = ind + self.step if ind <= self.size - 1 - self.step else ind + self.step - self.size

        for i in range(self.size):
            ind_value = self.slots[slot]
            if (not find_value_only and (ind_value is None or ind_value ^ value == 0)) or (find_value_only and ind_value is not None and ind_value ^ value == 0):
                return slot

            next_slot = slot + self.step

            slot = next_slot if slot <= self.size - 1 - self.step else next_slot - self.size

        return None

    def is_key(self, key):
        ind = self.seek_slot(key, True)
        return ind is not None

    def put(self, key, value):
        if self.count >= self.size * 0.75:
            self.__resize()

        key_ind = self.seek_slot(key)
        self.slots[key_ind] = key
        self.values[key_ind] = value
        self.count += 1

    def __resize(self):
        self.size *= 2
        cur_slots = self.slots
        cur_values = self.values

        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.count = 0

        for ind, s in enumerate(cur_slots):
            if s is not None:
                self.put(s, cur_values[ind])

    def get(self, key):
        ind = self.seek_slot(key, True)

        return self.values[ind] if ind is not None else None

    # Рефлексия задач задания 7:

    # Слияние двух упорядоченных списков в один
    # Задание выполнено верно, были добавлены функции, учитывающие возрастание или убывание списков

    # Проверка наличия заданного упорядоченного под-списка в текущем списке:
    # В решении не учтены моменты, когда продолжение подсписка искать уже бесполезно, например
    # из-за разницы больше/меньше или из-за длинны списков, само задание выполнено обычным линейным поиском

    # Ищем наиболее часто встречающееся значение в списке
    # При выполнении задания была допущена опечатка, решение оформлено правильно

    # Индекс заданного элемента в списке за O(log N).
    # Задание выполнено верно, для выполнения поиска использовался массив значений