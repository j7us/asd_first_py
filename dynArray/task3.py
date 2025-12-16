import ctypes

# Сложность удаления в худшем случае О(n) в лучшем O(1),
# Тоже касается и insert

class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

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
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i <0 or i > self.count:
            raise IndexError('Index is out of bounds')

        if self.count == self.capacity:
            self.resize(2 * self.capacity)

        self.copyFromIndex(i)
        self.array[i] = itm
        self.count += 1


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

        if i != self.count - 1:
            index = i + 1

            while index < self.count:
                self.array[index - 1] = self.array[index]
                index += 1

            self.array[self.count - 1] = None

        self.count -= 1

        new_size = int(self.capacity / 1.5)
        if self.count < (self.capacity / 2) and new_size >= 16:
            self.resize(new_size)

