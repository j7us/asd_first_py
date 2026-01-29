class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bit_array = 1 << f_len


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


    def is_value(self, str1):
        first_hash = self.hash1(str1)
        second_hash = self.hash2(str1)

        mask_for_hash_result = (1 << first_hash) | (1 << second_hash)

        return (mask_for_hash_result & self.bit_array) != 0