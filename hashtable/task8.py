class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

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
        ind = self.seek_slot(value)

        if ind is not None:
            self.slots[ind] = value

        return ind

    def find(self, value):
        ind = self.hash_fun(value)

        if self.slots[ind] == value:
            return ind

        return self.__find_slot_from_current(ind, value)

