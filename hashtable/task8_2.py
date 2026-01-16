# Задание 8
# задача 3
# Динамическая хэш-таблица
# время O(n)
class DynHashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.count = 0

    def hash_fun(self, value):
        ind = hash(value) % self.size
        return ind * -1 if ind < 0 else ind

    def seek_slot(self, value):
        ind = self.hash_fun(value)

        if self.slots[ind] is None:
            return ind

        return self.__find_slot_from_current(ind)

    def __find_slot_from_current(self, ind, value=None):
        slot = ind + self.step if ind <= self.size - 1 - self.step else ind + self.step - self.size

        for i in range(self.size):
            if self.slots[slot] == value:
                return slot

            next_slot = slot + self.step

            slot = next_slot if slot <= self.size - 1 - self.step else next_slot - self.size

        return None

    def put(self, value):
        if self.count >= self.size * 0.75:
            self.__resize()

        ind = self.seek_slot(value)

        if ind is not None:
            self.slots[ind] = value

        self.count += 1
        return ind

    def __resize(self):
        self.size *= 2
        cur_slots = self.slots
        self.slots = [None] * self.size
        self.count = 0

        for s in cur_slots:
            if s is not None:
                self.put(s)

    def find(self, value):
        ind = self.hash_fun(value)

        if self.slots[ind] == value:
            return ind

        return self.__find_slot_from_current(ind, value)


# Задание 8
# задача 4
# Использование нескольких хэщ функций
# При использовании нескольких функций у нас возможно будет больше скорость нахождения свободной ячейки
# благодаря почти уникальному шагу от второй хэш функции
class TwoHashHashTable:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.count = 0

    def hash_fun(self, value):
        ind = hash(value) % self.size
        return ind * -1 if ind < 0 else ind

    def second_hash_fun(self, value):
        ind = hash(value) % 97 + 1
        return ind * -1 if ind < 0 else ind

    def seek_slot(self, value):
        ind = self.hash_fun(value)

        if self.slots[ind] is None:
            return ind

        return self.__find_slot_from_current(ind)

    def __find_slot_from_current(self, ind, value=None):
        step = self.second_hash_fun(value)
        slot = ind + step if ind <= self.size - 1 - step else ind + step - self.size

        for i in range(self.size):
            if self.slots[slot] == value:
                return slot

            next_slot = slot + step

            slot = next_slot if slot <= self.size - 1 - step else next_slot - self.size

        return None

    def put(self, value):
        if self.count >= self.size * 0.75:
            self.__resize()

        ind = self.seek_slot(value)

        if ind is not None:
            self.slots[ind] = value

        self.count += 1
        return ind

    def __resize(self):
        self.size *= 2
        cur_slots = self.slots
        self.slots = [None] * self.size

        for s in cur_slots:
            if s is not None:
                self.put(s)

    def find(self, value):
        ind = self.hash_fun(value)

        if self.slots[ind] == value:
            return ind

        return self.__find_slot_from_current(ind, value)

# Задание 8
# задача 5
# Добавление соли
class SaltHashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.salt = 'asdb1414nfasm'

    def hash_fun(self, value):
        ind = hash(value + self.salt) % self.size
        return ind * -1 if ind < 0 else ind

    def seek_slot(self, value):
        ind = self.hash_fun(value)

        if self.slots[ind] is None:
            return ind

        return self.__find_slot_from_current(ind)

    def __find_slot_from_current(self, ind, value=None):
        slot = ind + self.step if ind <= self.size - 1 - self.step else ind + self.step - self.size

        for i in range(self.size):
            if self.slots[slot] == value:
                return slot

            next_slot = slot + self.step

            slot = next_slot if slot <= self.size - 1 - self.step else next_slot - self.size

        return None

    def put(self, value):
        ind = self.seek_slot(value)

        if ind is not None:
            self.slots[ind] = value

        return ind

    def find(self, value):
        ind = self.hash_fun(value)

        if self.slots[ind] == value:
            return ind

        return self.__find_slot_from_current(ind, value)

# Рефлексия задач задания 4:

# 4. Проверка строки на палиндром.
# Выполнено верно

# 5. Минимальный элемент деки за O(1).
# Задача выполнена неверно, не было предусмотрено удаление с конца как и говорится в решении,
# в тестах это также было не предусмотрено такое

# 6. Двусторонняя очередь на базе динамического массива.
# Насколько я понимаю используемый в основном задании массив и является динамическим, поэтому дополнительное
# задание было реализовано в основном

