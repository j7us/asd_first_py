import unittest

from powerset.task10 import PowerSet
from powerset.task10_2 import cartesian, intersection_with_multiple_sets, PowerSetBag


class PowerSetTest(unittest.TestCase):

    def setUp(self):
        self.powerset = PowerSet()

    def test_put(self):
        self.powerset.put('a')
        self.powerset.put('b')
        self.powerset.put('c')
        self.powerset.put('a')

        self.assertEqual(self.powerset.slots, dict.fromkeys(['a', 'b', 'c']))

    def test_get_empty(self):
        self.assertFalse(self.powerset.get('a'))

    def test_get_False(self):
        self.powerset.put('a')
        self.powerset.put('b')
        self.powerset.put('c')
        self.powerset.put('a')

        self.assertFalse(self.powerset.get('d'))

    def test_get(self):
        self.powerset.put('a')
        self.powerset.put('b')
        self.powerset.put('c')
        self.powerset.put('a')

        self.assertTrue(self.powerset.get('a'))

    def test_remove_empty(self):
        self.assertFalse(self.powerset.remove('a'))

    def test_remove_False(self):
        self.powerset.put('a')
        self.powerset.put('b')
        self.powerset.put('c')
        self.powerset.put('a')

        self.assertFalse(self.powerset.remove('d'))

    def test_remove(self):
        self.powerset.put('a')
        self.powerset.put('b')
        self.powerset.put('c')
        self.powerset.put('a')

        self.assertTrue(self.powerset.remove('a'))

    def test_intersection_empty(self):
        self.powerset.put('a')
        self.powerset.put('b')
        self.powerset.put('c')
        self.powerset.put('a')

        new_power = PowerSet()
        new_power.put('aa')
        new_power.put('bb')
        new_power.put('cc')

        res = self.powerset.intersection(new_power)

        self.assertEqual(res.size(), 0)

    def test_intersection_one(self):
        self.powerset.put('a')
        self.powerset.put('b')
        self.powerset.put('c')
        self.powerset.put('a')

        new_power = PowerSet()
        new_power.put('aa')
        new_power.put('b')
        new_power.put('cc')

        res = self.powerset.intersection(new_power)

        self.assertEqual(res.size(), 1)
        self.assertTrue(res.get('b'))

    def test_intersection_multiple(self):
        self.powerset.put('a')
        self.powerset.put('b')
        self.powerset.put('c')
        self.powerset.put('a')

        new_power = PowerSet()
        new_power.put('aa')
        new_power.put('b')
        new_power.put('cc')
        new_power.put('c')

        res = self.powerset.intersection(new_power)

        self.assertEqual(res.size(), 2)
        self.assertTrue(res.get('b'))
        self.assertTrue(res.get('c'))

    def test_union_empty(self):
        union = self.powerset.union(PowerSet())
        self.assertEqual(union.size(), 0)

    def test_union_first_not_empty(self):
        self.powerset.put('a')
        self.powerset.put('b')
        self.powerset.put('c')
        self.powerset.put('a')

        union = self.powerset.union(PowerSet())
        self.assertEqual(union.size(), 3)
        self.assertTrue(union.get('a'))
        self.assertTrue(union.get('c'))
        self.assertTrue(union.get('b'))

    def test_union_second_not_empty(self):
        new_power = PowerSet()
        new_power.put('aa')
        new_power.put('b')
        new_power.put('cc')
        new_power.put('c')

        union = self.powerset.union(new_power)
        self.assertEqual(union.size(), 4)
        self.assertTrue(union.get('aa'))
        self.assertTrue(union.get('cc'))
        self.assertTrue(union.get('c'))
        self.assertTrue(union.get('b'))

    def test_union(self):
        self.powerset.put('a')
        self.powerset.put('b')
        self.powerset.put('c')
        self.powerset.put('a')

        new_power = PowerSet()
        new_power.put('aa')
        new_power.put('b')
        new_power.put('cc')
        new_power.put('c')

        union = self.powerset.union(new_power)
        self.assertEqual(union.size(), 5)
        self.assertTrue(union.get('aa'))
        self.assertTrue(union.get('cc'))
        self.assertTrue(union.get('c'))
        self.assertTrue(union.get('a'))
        self.assertTrue(union.get('b'))

    def test_difference_empty(self):
        union = self.powerset.difference(PowerSet())
        self.assertEqual(union.size(), 0)

    def test_difference_first_not_empty(self):
        self.powerset.put('a')
        self.powerset.put('b')
        self.powerset.put('c')
        self.powerset.put('a')

        union = self.powerset.difference(PowerSet())
        self.assertEqual(union.size(), 3)
        self.assertTrue(union.get('a'))
        self.assertTrue(union.get('b'))
        self.assertTrue(union.get('c'))

    def test_difference_second_not_empty(self):
        new_power = PowerSet()
        new_power.put('aa')
        new_power.put('b')
        new_power.put('cc')
        new_power.put('c')

        union = self.powerset.difference(new_power)
        self.assertEqual(union.size(), 0)

    def test_difference(self):
        self.powerset.put('a')
        self.powerset.put('b')
        self.powerset.put('c')
        self.powerset.put('a')
        self.powerset.put('d')

        new_power = PowerSet()
        new_power.put('aa')
        new_power.put('b')
        new_power.put('cc')
        new_power.put('c')

        union = self.powerset.difference(new_power)
        self.assertEqual(union.size(), 2)
        self.assertTrue(union.get('a'))
        self.assertTrue(union.get('d'))

    def test_issubset_both_empty(self):
        self.assertFalse(self.powerset.issubset(PowerSet()))

    def test_issubset_second_empty(self):
        self.powerset.put('a')
        self.powerset.put('b')
        self.powerset.put('c')
        self.powerset.put('a')
        self.powerset.put('d')

        self.assertFalse(self.powerset.issubset(PowerSet()))

    def test_issubset_True(self):
        self.powerset.put('a')
        self.powerset.put('b')
        self.powerset.put('c')
        self.powerset.put('g')
        self.powerset.put('d')

        new_power = PowerSet()
        new_power.put('b')
        new_power.put('c')

        self.assertTrue(self.powerset.issubset(new_power))

    def test_issubset_False(self):
        self.powerset.put('a')
        self.powerset.put('b')
        self.powerset.put('c')
        self.powerset.put('g')
        self.powerset.put('d')

        new_power = PowerSet()
        new_power.put('p')
        new_power.put('m')

        self.assertFalse(self.powerset.issubset(new_power))

    def test_issubset_False_with_few_el(self):
        self.powerset.put('a')
        self.powerset.put('b')
        self.powerset.put('c')
        self.powerset.put('g')
        self.powerset.put('d')

        new_power = PowerSet()
        new_power.put('a')
        new_power.put('b')
        new_power.put('c')
        new_power.put('g')
        new_power.put('d')
        new_power.put('p')
        new_power.put('m')

        self.assertFalse(self.powerset.issubset(new_power))

    def test_equal_both_empty(self):
        self.assertTrue(self.powerset.equals(PowerSet()))

    def test_equal_first_not_empty(self):
        self.powerset.put('a')
        self.powerset.put('b')
        self.powerset.put('c')
        self.powerset.put('g')
        self.powerset.put('d')

        self.assertFalse(self.powerset.equals(PowerSet()))

    def test_equal_second_not_empty(self):
        new_power = PowerSet()
        new_power.put('a')
        new_power.put('b')
        new_power.put('c')
        new_power.put('g')
        new_power.put('d')
        new_power.put('p')
        new_power.put('m')

        self.assertFalse(self.powerset.equals(new_power))

    def test_equal_True(self):
        self.powerset.put('a')
        self.powerset.put('b')
        self.powerset.put('c')
        self.powerset.put('g')
        self.powerset.put('d')

        new_power = PowerSet()
        new_power.put('a')
        new_power.put('b')
        new_power.put('c')
        new_power.put('g')
        new_power.put('d')

        self.assertTrue(self.powerset.equals(new_power))

    def test_equal_first_more_el(self):
        self.powerset.put('a')
        self.powerset.put('b')
        self.powerset.put('c')
        self.powerset.put('g')
        self.powerset.put('d')

        new_power = PowerSet()
        new_power.put('a')
        new_power.put('b')
        new_power.put('c')
        new_power.put('g')

        self.assertFalse(self.powerset.equals(new_power))

    def test_equal_second_more_el(self):
        self.powerset.put('a')
        self.powerset.put('b')

        new_power = PowerSet()
        new_power.put('a')
        new_power.put('b')
        new_power.put('c')
        new_power.put('g')

        self.assertFalse(self.powerset.equals(new_power))

    def test_cartesian(self):
        self.powerset.put('a')
        self.powerset.put('b')
        self.powerset.put('c')
        self.powerset.put('g')
        self.powerset.put('d')

        new_power = PowerSet()
        new_power.put('a')
        new_power.put('b')
        new_power.put('c')
        new_power.put('g')

        res = cartesian(self.powerset, new_power)

        self.assertEqual(res.size(), 20)

    def test_intersection_with_multiple_sets(self):
        new_power_1 = PowerSet()
        new_power_1.put('a')
        new_power_1.put('b')
        new_power_1.put('c')
        new_power_1.put('g')

        new_power_2 = PowerSet()
        new_power_2.put('a')
        new_power_2.put('b')
        new_power_2.put('c')
        new_power_2.put('g')

        new_power_3 = PowerSet()
        new_power_3.put('a')
        new_power_3.put('b')

        res = intersection_with_multiple_sets([new_power_1, new_power_2, new_power_3])

        self.assertEqual(res.size(), 2)
        self.assertTrue(res.get('b'))
        self.assertTrue(res.get('a'))

    def test_bag(self):
        set_test = PowerSetBag()
        set_test.put('a')
        set_test.put('b')
        set_test.put('c')
        set_test.put('a')
        set_test.put('a')

        set_test.remove('b')
        set_test.remove('a')

        res = set_test.get_all_with_counts()

        self.assertEqual(len(res), 2)

