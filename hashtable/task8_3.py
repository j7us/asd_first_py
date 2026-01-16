import unittest

from hashtable.task8 import HashTable
from hashtable.task8_2 import DynHashTable, TwoHashHashTable


class HashTableTest(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable(8, 3)

    def test_hash(self):
        test = ['Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'a', 'b', 'c', 'd', 'e', 'f']

        for t in test:
            res = self.hash_table.hash_fun(t)
            self.assertTrue(0 <= res <= 7)

    def test_seek_slot(self):
        first_hash = self.hash_table.hash_fun('a')
        self.hash_table.put('a')

        ind = self.hash_table.seek_slot('a')
        self.assertNotEquals(first_hash, ind)

    def test_seek_slot_None(self):
        for i in range(8):
            self.hash_table.put('a')

        ind = self.hash_table.seek_slot('a')
        self.assertIsNone(ind)

    def test_put(self):
        for i in range(8):
            self.hash_table.put('a')

        res = self.hash_table.put('a')

        self.assertIsNone(res)

    def test_find(self):
        test = ['a', 'b', 'c', 'd', 'e', 'f']

        for t in test:
            self.hash_table.put(t)

        g_ind = self.hash_table.put('g')

        find_ind = self.hash_table.find('g')

        self.assertEqual(g_ind, find_ind)

    def test_find_empty(self):
        find_ind = self.hash_table.find('g')
        self.assertIsNone(find_ind)

    def test_dyn_hash_table(self):
        dyn = DynHashTable(8, 3)
        for i in range(8):
            dyn.put('a')

        self.assertEqual(dyn.size, 16)

