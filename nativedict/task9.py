class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.count = 0
        self.step = 1

    def hash_fun(self, key):
        ind = hash(key) % self.size
        return ind * -1 if ind < 0 else ind

    def seek_slot(self, value, to_find):
        ind = self.hash_fun(value)

        if self.slots[ind] in to_find:
            return ind

        return self.__find_slot_from_current(ind, to_find)

    def __find_slot_from_current(self, ind, value):
        slot = ind + self.step if ind <= self.size - 1 - self.step else ind + self.step - self.size

        for i in range(self.size):
            if self.slots[slot] in value:
                return slot

            next_slot = slot + self.step

            slot = next_slot if slot <= self.size - 1 - self.step else next_slot - self.size

        return None

    def is_key(self, key):
        ind = self.seek_slot(key, [key])
        return ind is not None

    def put(self, key, value):
        if self.count >= self.size * 0.75:
            self.__resize()

        key_ind = self.seek_slot(key, [key, None])
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
        ind = self.seek_slot(key, [key])

        return self.values[ind] if ind is not None else None

