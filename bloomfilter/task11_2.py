# Задание 11
# задача 2
# Слияние фильтров
# время O(n)
def combine_filters(filters):
    result_bloom_filter = filters[0]

    for f in filters[1:]:
        result_bloom_filter = result_bloom_filter | f

    return result_bloom_filter

# Задание 11
# задача 3
# Фильтр с удалением элементов
# время O(1)
class BloomFilterWithDelete:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bit_array = 1 << f_len
        self.bit_counter = [0] * self.filter_len


    def hash1(self, str1):
        return self.__calculate_standart_hash_with_random_int(str1, 17)

    def hash2(self, str1):
        return self.__calculate_standart_hash_with_random_int(str1, 223)

    def __calculate_standart_hash_with_random_int(self, val, rand):
        res = 0

        for c in val:
            code = ord(c)
            res = res * rand + code

        return res % self.filter_len

    def add(self, str1):
        first_hash = self.hash1(str1)
        second_hash = self.hash2(str1)

        mask_for_hash_result = (1 << first_hash) | (1 << second_hash)
        self.bit_array = self.bit_array | mask_for_hash_result

        self.bit_counter[first_hash] += 1
        self.bit_counter[second_hash] += 1


    def is_value(self, str1):
        first_hash = self.hash1(str1)
        second_hash = self.hash2(str1)

        mask_for_hash_result = (1 << first_hash) | (1 << second_hash)

        return (mask_for_hash_result & self.bit_array) != 0

    def remove(self, str1):
        first_hash = self.hash1(str1)
        second_hash = self.hash2(str1)

        f_res = self.bit_counter[first_hash]
        s_res = self.bit_counter[second_hash]

        counter_stage_done = False

        if f_res > s_res:
            self.bit_counter[first_hash] -= 1
            self.bit_counter[second_hash] -= 1
            counter_stage_done = True

        if counter_stage_done and (self.bit_counter[first_hash] == 0 or self.bit_counter[second_hash] == 0):
            first_mask = (1 << first_hash) if self.bit_counter[first_hash] == 0 else 0
            second_mask = (1 << second_hash) if self.bit_counter[second_hash] == 0 else 0

            self.bit_array = self.bit_array ^ first_mask ^ second_mask

    # Задание 11
    # задача 4
    # Восстановление данных из фильтра Блюма
    # Пока было выработано два варианта:
    # 1) Если примерное направление значений нам известно, можно попытаться восстановить методом подбора
    # 2) Если направление мысли нам не известно, то можно собрать все пары активных битов в массиве и искать такие значения,
    # у которых две хэш функции дадут сочетание этих битов


    # Рефлексия задач задания 9:

    # Словарь с использованием упорядоченного списка по ключу.
    # В данном случае я использовал класс Bucket, в котором было переопределено сравнение элементов и класс
    # имел два поля, чтобы в упорядоченный список можно было сразу добавить и ключ и значение, казалось, что такой вариант
    # может немного выигрывать по памяти.

