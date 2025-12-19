import ctypes
import math


# Задание 3
# задача 5
# Реализация банковского метода
#
class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.bank = 0
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def calculate_changes_count(self, new_capacity):
        self.bank -= self.get_resize_cost(new_capacity)

    def get_resize_cost(self, new_capacity):
        return 2 ** int(math.log2(new_capacity))

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            new_capacity = 2 * self.capacity
            self.calculate_changes_count(new_capacity)
            self.resize(new_capacity)
        self.array[self.count] = itm
        self.count += 1
        self.bank += 3

    def insert(self, i, itm):
        if i <0 or i > self.count:
            raise IndexError('Index is out of bounds')

        if self.count == self.capacity:
            new_capacity = 2 * self.capacity
            self.calculate_changes_count(new_capacity)
            self.resize(new_capacity)

        self.copyFromIndex(i)
        self.array[i] = itm
        self.count += 1
        self.bank += 3


    def copyFromIndex(self, i):
        if i == self.count:
            return

        index = self.count - 1

        while index >= i:
            self.array[index + 1] = self.array[index]
            index -= 1

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')

        self.array[i] = None

        index = i + 1

        while index < self.count:
            self.array[index - 1] = self.array[index]
            index += 1

        self.count -= 1
        self.bank += 3

        new_size = int(self.capacity / 1.5)
        if self.count < (self.capacity / 2) and new_size >= 16:
            self.calculate_changes_count(new_size)
            self.resize(new_size)



# Задание 3
# задача 6
# Многомерный динамический массив
#
class MultiDynArray:

    def __init__(self, capacity_levels: list[int]):
        capacity = 1

        for cap in capacity_levels:
            capacity *= cap

        self.count = 0
        self.capacity = capacity
        self.array = self.make_array(capacity)


    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        index_to_find = self.__calculate_index(i) if isinstance(i, tuple) else i

        if index_to_find > self.capacity:
            raise IndexError('Index is out of bounds')

        return self.array[index_to_find]

    def __setitem__(self, key, value):
        if self.count == self.capacity:
            self.resize(self.capacity * 2)

        index_to_find = self.__calculate_index(key) if isinstance(key, tuple) else key

        if index_to_find > self.capacity:
            raise IndexError('Index is out of bounds')

        self.array[index_to_find] = value
        self.count += 1


    def __calculate_index(self, ind: tuple):
        calculated_ind = 1

        for i in range(len(ind)):
            calculated_ind *= ind[i]

        return calculated_ind

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

# Рефлексия задачи 1.8 первого задания: задача выполнена верно, решение соответствует представленному

