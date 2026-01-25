from __future__ import annotations
from typing import Any

class PowerSet:

    def __init__(self) -> None:
        self.slots = {}

    def size(self) -> int:
        return len(self.slots)

    def put(self, value: Any) -> None:
        self.slots.setdefault(value)

    def get(self, value: Any) -> bool:
        return value in self.slots

    def remove(self, value: Any) -> bool:
        res = False

        if value in self.slots:
            del self.slots[value]
            res = True

        return res

    def intersection(self, set2: PowerSet) -> PowerSet:
        result_set = PowerSet()

        for s in self.slots:
            if set2.get(s):
                result_set.put(s)

        return result_set

    def union(self, set2: PowerSet) -> PowerSet:
        result_set = PowerSet()

        for s in self.slots:
            result_set.put(s)

        for s in set2.slots:
            result_set.put(s)

        return result_set

    def difference(self, set2: PowerSet) -> PowerSet:
        result_set = PowerSet()

        for s in self.slots:
            if not set2.get(s):
                result_set.put(s)

        return result_set

    def issubset(self, set2: PowerSet) -> bool:
        if set2.size() == 0:
            return False

        for s in set2.slots:
            if s not in self.slots:
                return False

        return True

    def equals(self, set2: PowerSet) -> bool:
        if not len(self.slots) == set2.size():
            return False

        for s in self.slots:
            if not set2.get(s):
                return False

        return True