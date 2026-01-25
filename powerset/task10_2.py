from __future__ import annotations
from typing import Any
from powerset.task10 import PowerSet

# Задание 10
# задача 4
# Декартово произведение множеств
# Время O(n + m), n и m - длины множеств
def cartesian(set1: PowerSet, set2: PowerSet):
    result_set = PowerSet()

    for s in set1.slots:
        for p in set2.slots:
            result_set.put((s,p))

    return result_set

# Задание 10
# задача 5
# Пересечение любых трёх и более множеств
# Время O(n * m), n самое короткое множество, m - всего множеств
def intersection_with_multiple_sets(sets):
    if len(sets) < 3:
        raise Exception("Список должен содержать не менее трех множеств")

    result_set = PowerSet()

    base = min(sets, key=lambda s: s.size())

    for x in base.slots:
        if val_in_all_sets(sets,x):
            result_set.put(x)

    return result_set

def val_in_all_sets(sets, val):
    res = True

    for s in sets:
        if not s.get(val):
            res = False
            break

    return res


# Задание 10
# задача 6
# Мульти-множество (Bag)
# Удаление и добавление происходит за O(1)
class PowerSetBag:

    def __init__(self) -> None:
        self.slots = {}
        self.remove_methods = {
            'dec': self.__dec_value,
            'del': self.__del_value
        }

    def __dec_value(self, val):
        self.slots[val] -= 1

    def __del_value(self, val):
        del self.slots[val]

    def put(self, value: Any) -> None:
        self.slots[value] = self.slots.get(value, 0) + 1

    def get(self, value: Any) -> bool:
        return value in self.slots

    def remove(self, value: Any) -> bool:
        res = False

        if value in self.slots:
            count = self.slots[value]

            del_type = 'dec' if count > 1 else 'del'

            self.remove_methods[del_type](value)

            res = True

        return res

    def get_all_with_counts(self):
        res = []

        for k, v in self.slots.items():
            res.append((k,v))

        return res

# Рефлексия задач задания 8:

# Динамическая хэш-таблица.
# Задание выполнено верно

# ddos хэш-таблицы и соль
# Задание выполнено с добавлением соли, но в этом случае соль была статической,
# так как не подумал про хранение динамической соли вместе со значением

