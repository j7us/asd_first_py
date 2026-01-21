import unittest

from nativedict.task9 import NativeDictionary
from nativedict.task9_2 import BitNativeDictionary


class TestNativeDictionary(unittest.TestCase):
    def setUp(self):
        self.nd = NativeDictionary(4)

    def test_put_one(self):
        self.nd.put('a', 1)

        sl_ind = self.nd.slots.index('a')
        val_ind = self.nd.values.index(1)

        self.assertEqual(sl_ind, val_ind)

    def test_put_max_size(self):
        k_v_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

        for k_v in k_v_list:
            self.nd.put(k_v[0], k_v[1])

        for k_v in k_v_list:
            sl_ind = self.nd.slots.index(k_v[0])
            val_ind = self.nd.values.index(k_v[1])

            self.assertEqual(sl_ind, val_ind)

        self.assertEqual(len(self.nd.slots), 8)
        self.assertEqual(len(self.nd.values), 8)

    def test_put_max_size_plus_one(self):
        k_v_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

        for k_v in k_v_list:
            self.nd.put(k_v[0], k_v[1])

        for k_v in k_v_list:
            sl_ind = self.nd.slots.index(k_v[0])
            val_ind = self.nd.values.index(k_v[1])

            self.assertEqual(sl_ind, val_ind)

        self.assertEqual(len(self.nd.slots), 8)

    def test_put_same_key(self):
        self.nd.put('a', 1)
        self.nd.put('a', 2)

        k_ind = self.nd.slots.index('a')
        old_val_exist = 1 in self.nd.values

        self.assertEqual(self.nd.values[k_ind], 2)
        self.assertFalse(old_val_exist)

    def test_is_key_False(self):
        self.assertFalse(self.nd.is_key('a'))

    def test_is_key_True(self):
        k_v_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

        for k_v in k_v_list:
            self.nd.put(k_v[0], k_v[1])

        self.assertTrue(self.nd.is_key('c'))

    def test_get_empty(self):
        self.assertIsNone(self.nd.get('a'))

    def test_get(self):
        k_v_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

        for k_v in k_v_list:
            self.nd.put(k_v[0], k_v[1])

        self.assertEqual(self.nd.get('d'), 4)

    def test_BitNativeDictionary(self):
        dict = BitNativeDictionary(4)

        k_v_list = [(0b0011, 1), (0b1101, 2), (0b0001, 3), (0b1000, 4), (0b0100, 5)]

        for k_v in k_v_list:
            dict.put(k_v[0], k_v[1])

        for k_v in k_v_list:
            sl_ind = dict.slots.index(k_v[0])
            val_ind = dict.values.index(k_v[1])

            self.assertEqual(sl_ind, val_ind)

    def test_BitNativeDictionary_put_and_get(self):
        dict = BitNativeDictionary(4)

        dict.put(0b0011, 1)
        dict.put(0b0011, 2)

        val = dict.get(0b0011)

        self.assertEqual(val, 2)

