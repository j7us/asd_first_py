import unittest

from cache.task12 import NativeCache


class TestNativeCache(unittest.TestCase):

    def setUp(self):
        self.ch = NativeCache(3)

    def test_put(self):
        cache = self.ch

        cache.put('a', 1)
        cache.put('b', 2)
        cache.put('c', 3)

        self.assertTrue('a' in cache.slots)
        self.assertTrue('b' in cache.slots)
        self.assertTrue('c' in cache.slots)
        self.assertEqual(len(cache.slots), 3)

    def test_hit(self):
        cache = self.ch

        cache.put('a', 1)
        cache.put('b', 2)
        cache.put('c', 3)

        cache.get('a')
        cache.get('b')
        cache.get('c')
        cache.get('a')
        cache.get('b')

        hits = {'a': 2, 'b': 2, 'c': 1}

        for ind, val in enumerate(cache.slots):
            self.assertEqual(cache.hits[ind], hits[val])

    def test_replace(self):
        cache = self.ch

        cache.put('a', 1)
        cache.put('b', 2)
        cache.put('c', 3)

        cache.get('a')
        cache.get('b')
        cache.get('c')
        cache.get('a')
        cache.get('b')

        cache.put('d', 4)

        self.assertEqual(cache.get('d'), 4)
        self.assertIsNone(cache.get('c'))

