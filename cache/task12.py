class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        ind = hash(key) % self.size
        return ind * -1 if ind < 0 else ind

    def seek_slot(self, value, to_find):
        ind = self.hash_fun(value)

        if self.slots[ind] in to_find:
            return ind

        return self.__find_slot_from_current(ind, to_find)

    def __find_slot_from_current(self, ind, value):
        slot = ind + 1 if ind <= self.size - 1 - 1 else ind + 1 - self.size

        for i in range(self.size):
            if self.slots[slot] in value:
                return slot

            next_slot = slot + 1

            slot = next_slot if slot <= self.size - 2 else next_slot - self.size

        return -1

    def put(self, key, value):
        key_ind = -1

        while key_ind < 0:
            key_ind = self.seek_slot(key, [key, None])

            if key_ind < 0:
                self.__remove_unused()

        self.slots[key_ind] = key
        self.values[key_ind] = value

    def __remove_unused(self):
        cur_min = -1
        ind_min = -1

        for ind, f in enumerate(self.hits):
            if cur_min < 0 or f < cur_min:
                cur_min = f
                ind_min = ind

        self.hits[ind_min] = 0
        self.values[ind_min] = None
        self.slots[ind_min] = None

    def get(self, key):
        ind = self.seek_slot(key, [key])

        res = self.values[ind] if ind >= 0 else None

        if res is not None:
            self.hits[ind] += 1

        return res

