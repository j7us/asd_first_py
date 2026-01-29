import unittest

from bloomfilter.task11 import BloomFilter


class BloomFilterTest(unittest.TestCase):

    def setUp(self):
        self.filter = BloomFilter(32)

    def test_add(self):
        self.filter.add("0123456789")
        self.filter.add("1234567890")
        self.filter.add("2345678901")
        self.filter.add("3456789012")
        self.filter.add("4567890123")
        self.filter.add("5678901234")
        self.filter.add("6789012345")
        self.filter.add("7890123456")
        self.filter.add("8901234567")
        self.filter.add("9012345678")

        self.assertTrue(self.filter.bit_array | 0)

    def test_is_value(self):
        self.filter.add("0123456789")
        self.filter.add("1234567890")
        self.filter.add("2345678901")
        self.filter.add("3456789012")
        self.filter.add("4567890123")
        self.filter.add("5678901234")
        self.filter.add("6789012345")
        self.filter.add("7890123456")
        self.filter.add("8901234567")
        self.filter.add("9012345678")

        self.assertTrue(self.filter.is_value("0123456789"))
        self.assertTrue(self.filter.is_value("1234567890"))
        self.assertTrue(self.filter.is_value("2345678901"))
        self.assertTrue(self.filter.is_value("3456789012"))
        self.assertTrue(self.filter.is_value("4567890123"))
        self.assertTrue(self.filter.is_value("5678901234"))
        self.assertTrue(self.filter.is_value("6789012345"))
        self.assertTrue(self.filter.is_value("7890123456"))
        self.assertTrue(self.filter.is_value("8901234567"))
        self.assertTrue(self.filter.is_value("9012345678"))

    def test_is_value_empty(self):
        self.assertFalse(self.filter.is_value("first"))

    def test_is_value_False(self):
        self.filter.add("a")
        self.filter.add("b")

        self.assertFalse(self.filter.is_value("c"))
