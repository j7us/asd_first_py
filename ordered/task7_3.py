import unittest

from ordered.task7 import OrderedList, OrderedStringList
from ordered.task7_2 import OrderedListWithDuplicateRemove, merge_lists, OrderedListWithSubListFunc, find_popular_value, \
    OrderedListWithIndex


class OrderedListTest(unittest.TestCase):

    def setUp(self):
        self.list = OrderedList(True)
        self.str_list = OrderedStringList(True)

    def test_add_asc_True(self):
        list_ord = self.list

        list_ord.add(1)
        list_ord.add(2)
        list_ord.add(-1)
        list_ord.add(1)

        node_val = [-1,1,1,2]
        result = list(map(lambda x: x.value, list_ord.get_all()))

        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 4)
        self.assertEqual(list_ord.head.value, -1)
        self.assertEqual(list_ord.tail.value, 2)

    def test_add_asc_True_same(self):
        list_ord = self.list

        list_ord.add(1)
        list_ord.add(1)
        list_ord.add(1)

        node_val = [1, 1, 1]
        result = list(map(lambda x: x.value, list_ord.get_all()))

        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 3)
        self.assertEqual(list_ord.head.value, 1)
        self.assertEqual(list_ord.tail.value, 1)

    def test_add_asc_True_head(self):
        list_ord = self.list

        list_ord.add(-1)
        list_ord.add(5)
        list_ord.add(110)

        list_ord.add(-110)

        node_val = [-110, -1, 5, 110]
        result = list(map(lambda x: x.value, list_ord.get_all()))

        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 4)
        self.assertEqual(list_ord.head.value, -110)
        self.assertEqual(list_ord.tail.value, 110)

    def test_add_asc_True_tail(self):
        list_ord = self.list

        list_ord.add(-1)
        list_ord.add(5)
        list_ord.add(110)

        list_ord.add(120)

        node_val = [-1, 5, 110, 120]
        result = list(map(lambda x: x.value, list_ord.get_all()))

        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 4)
        self.assertEqual(list_ord.head.value, -1)
        self.assertEqual(list_ord.tail.value, 120)

    def test_add_asc_False(self):
        list_ord = self.list
        list_ord.clean(False)

        list_ord.add(1)
        list_ord.add(2)
        list_ord.add(-1)
        list_ord.add(1)

        node_val = [2, 1, 1, -1]
        result = list(map(lambda x: x.value, list_ord.get_all()))

        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 4)
        self.assertEqual(list_ord.head.value, 2)
        self.assertEqual(list_ord.tail.value, -1)

    def test_add_asc_False_same(self):
        list_ord = self.list
        list_ord.clean(False)

        list_ord.add(1)
        list_ord.add(1)
        list_ord.add(1)

        node_val = [1, 1, 1]
        result = list(map(lambda x: x.value, list_ord.get_all()))

        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 3)
        self.assertEqual(list_ord.head.value, 1)
        self.assertEqual(list_ord.tail.value, 1)

    def test_add_asc_False_head(self):
        list_ord = self.list
        list_ord.clean(False)

        list_ord.add(-1)
        list_ord.add(5)
        list_ord.add(110)

        list_ord.add(120)

        node_val = [120, 110, 5, -1]
        result = list(map(lambda x: x.value, list_ord.get_all()))

        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 4)
        self.assertEqual(list_ord.head.value, 120)
        self.assertEqual(list_ord.tail.value, -1)

    def test_add_asc_False_tail(self):
        list_ord = self.list
        list_ord.clean(False)

        list_ord.add(-1)
        list_ord.add(5)
        list_ord.add(110)

        list_ord.add(-110)

        result = list(map(lambda x: x.value, list_ord.get_all()))
        node_val = [110, 5, -1, -110]

        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 4)
        self.assertEqual(list_ord.head.value, 110)
        self.assertEqual(list_ord.tail.value, -110)

    def test_clean(self):
        list_ord = self.list

        list_ord.add(-1)
        list_ord.add(5)
        list_ord.add(110)

        list_ord.clean(True)

        self.assertEqual(list_ord.len(), 0)
        self.assertIsNone(list_ord.head)
        self.assertIsNone(list_ord.tail)

    def test_delete_empty(self):
        list_ord = self.list

        list_ord.delete(15)

        self.assertEqual(list_ord.len(), 0)
        self.assertIsNone(list_ord.head)
        self.assertIsNone(list_ord.tail)

    def test_delete_none(self):
        list_ord = self.list

        list_ord.add(-1)
        list_ord.add(5)
        list_ord.add(110)
        list_ord.add(-110)

        list_ord.delete(15)

        result = list(map(lambda x: x.value, list_ord.get_all()))
        node_val = [-110, -1, 5, 110]

        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 4)
        self.assertEqual(list_ord.head.value, -110)
        self.assertEqual(list_ord.tail.value, 110)

    def test_delete_head(self):
        list_ord = self.list

        list_ord.add(-1)
        list_ord.add(5)
        list_ord.add(110)
        list_ord.add(-110)

        list_ord.delete(-110)

        result = list(map(lambda x: x.value, list_ord.get_all()))
        node_val = [-1, 5, 110]

        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 3)
        self.assertEqual(list_ord.head.value, -1)
        self.assertEqual(list_ord.tail.value, 110)

    def test_delete_tail(self):
        list_ord = self.list

        list_ord.add(-1)
        list_ord.add(5)
        list_ord.add(110)
        list_ord.add(-110)

        list_ord.delete(110)

        result = list(map(lambda x: x.value, list_ord.get_all()))
        node_val = [-110, -1, 5]

        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 3)
        self.assertEqual(list_ord.head.value, -110)
        self.assertEqual(list_ord.tail.value, 5)

    def test_delete_middle(self):
        list_ord = self.list

        list_ord.add(-1)
        list_ord.add(5)
        list_ord.add(110)
        list_ord.add(50)
        list_ord.add(-110)

        list_ord.delete(50)

        result = list(map(lambda x: x.value, list_ord.get_all()))
        node_val = [-110, -1, 5, 110]

        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 4)
        self.assertEqual(list_ord.head.value, -110)
        self.assertEqual(list_ord.tail.value, 110)

    def test_delete_middle_duplicate(self):
        list_ord = self.list

        list_ord.add(-1)
        list_ord.add(5)
        list_ord.add(110)
        list_ord.add(-110)
        list_ord.add(-110)

        list_ord.delete(-110)

        result = list(map(lambda x: x.value, list_ord.get_all()))
        node_val = [-110, -1, 5, 110]

        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 4)
        self.assertEqual(list_ord.head.value, -110)
        self.assertEqual(list_ord.tail.value, 110)

    def test_find_empty(self):
        list_ord = self.list

        node = list_ord.find(15)

        self.assertIsNone(node)
        self.assertEqual(list_ord.len(), 0)
        self.assertIsNone(list_ord.head)
        self.assertIsNone(list_ord.tail)

    def test_find_none(self):
        list_ord = self.list

        list_ord.add(-1)
        list_ord.add(5)
        list_ord.add(110)
        list_ord.add(-110)

        node = list_ord.find(2)

        result = list(map(lambda x: x.value, list_ord.get_all()))
        node_val = [-110, -1, 5, 110]

        self.assertIsNone(node)
        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 4)
        self.assertEqual(list_ord.head.value, -110)
        self.assertEqual(list_ord.tail.value, 110)

    def test_find_none_False(self):
        list_ord = self.list
        list_ord.clean(False)

        list_ord.add(-1)
        list_ord.add(5)
        list_ord.add(110)
        list_ord.add(-110)

        node = list_ord.find(105)

        result = list(map(lambda x: x.value, list_ord.get_all()))
        node_val = [110, 5, -1, -110]

        self.assertIsNone(node)
        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 4)
        self.assertEqual(list_ord.head.value, 110)
        self.assertEqual(list_ord.tail.value, -110)

    def test_find(self):
        list_ord = self.list

        list_ord.add(-1)
        list_ord.add(5)
        list_ord.add(110)
        list_ord.add(-110)

        node = list_ord.find(5)

        result = list(map(lambda x: x.value, list_ord.get_all()))
        node_val = [-110, -1, 5, 110]

        self.assertEqual(node.value, 5)
        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 4)
        self.assertEqual(list_ord.head.value, -110)
        self.assertEqual(list_ord.tail.value, 110)

    def test_len_empty(self):
        list_ord = self.list

        self.assertEqual(list_ord.len(), 0)

    def test_len(self):
        list_ord = self.list

        list_ord.add(-1)
        list_ord.add(5)
        list_ord.add(110)
        list_ord.add(-110)

        list_ord.delete(110)
        list_ord.delete(-110)
        list_ord.delete(5)

        self.assertEqual(list_ord.len(), 1)

    def test_str_add_asc_True(self):
        list_ord = self.str_list

        list_ord.add('a')
        list_ord.add('b')
        list_ord.add('d')

        list_ord.add('c')

        node_val = ['a', 'b', 'c', 'd']
        result = list(map(lambda x: x.value, list_ord.get_all()))

        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 4)
        self.assertEqual(list_ord.head.value, 'a')
        self.assertEqual(list_ord.tail.value, 'd')

    def test_str_add_asc_True_same(self):
        list_ord = self.str_list

        list_ord.add('a')
        list_ord.add('a')
        list_ord.add('a')

        node_val = ['a', 'a', 'a']
        result = list(map(lambda x: x.value, list_ord.get_all()))

        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 3)
        self.assertEqual(list_ord.head.value, 'a')
        self.assertEqual(list_ord.tail.value, 'a')

    def test_str_add_asc_True_head(self):
        list_ord = self.str_list

        list_ord.add('b')
        list_ord.add('c')
        list_ord.add('d')

        list_ord.add('a')

        node_val = ['a', 'b', 'c', 'd']
        result = list(map(lambda x: x.value, list_ord.get_all()))

        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 4)
        self.assertEqual(list_ord.head.value, 'a')
        self.assertEqual(list_ord.tail.value, 'd')

    def test_str_add_asc_True_tail(self):
        list_ord = self.str_list

        list_ord.add('a')
        list_ord.add('b')
        list_ord.add('c')

        list_ord.add('d')

        node_val = ['a', 'b', 'c', 'd']
        result = list(map(lambda x: x.value, list_ord.get_all()))

        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 4)
        self.assertEqual(list_ord.head.value, 'a')
        self.assertEqual(list_ord.tail.value, 'd')

    def test_str_add_asc_False(self):
        list_ord = self.str_list
        list_ord.clean(False)

        list_ord.add('a')
        list_ord.add('b')
        list_ord.add('d')
        list_ord.add('c')

        node_val = ['d', 'c', 'b', 'a']
        result = list(map(lambda x: x.value, list_ord.get_all()))

        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 4)
        self.assertEqual(list_ord.head.value, 'd')
        self.assertEqual(list_ord.tail.value, 'a')

    def test_str_add_asc_False_same(self):
        list_ord = self.str_list
        list_ord.clean(False)

        list_ord.add('a')
        list_ord.add('a')
        list_ord.add('a')

        node_val = ['a', 'a', 'a']
        result = list(map(lambda x: x.value, list_ord.get_all()))

        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 3)
        self.assertEqual(list_ord.head.value, 'a')
        self.assertEqual(list_ord.tail.value, 'a')

    def test_str_add_asc_False_head(self):
        list_ord = self.str_list
        list_ord.clean(False)

        list_ord.add('a')
        list_ord.add('b')
        list_ord.add('c')

        list_ord.add('d')

        node_val = ['d', 'c', 'b', 'a']
        result = list(map(lambda x: x.value, list_ord.get_all()))

        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 4)
        self.assertEqual(list_ord.head.value, 'd')
        self.assertEqual(list_ord.tail.value, 'a')

    def test_str_add_asc_False_tail(self):
        list_ord = self.str_list
        list_ord.clean(False)

        list_ord.add('b')
        list_ord.add('c')
        list_ord.add('d')

        list_ord.add('a')

        result = list(map(lambda x: x.value, list_ord.get_all()))
        node_val = ['d', 'c', 'b', 'a']

        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 4)
        self.assertEqual(list_ord.head.value, 'd')
        self.assertEqual(list_ord.tail.value, 'a')

    def test_duplicate_remove(self):
        list_ord = OrderedListWithDuplicateRemove(True)
        list_ord.add(1)
        list_ord.add(1)
        list_ord.add(1)
        list_ord.add(2)
        list_ord.add(2)
        list_ord.add(2)
        list_ord.add(3)
        list_ord.add(3)
        list_ord.add(3)

        list_ord.remove_duplicates()

        result = list(map(lambda x: x.value, list_ord.get_all()))
        node_val = [1, 2, 3]

        self.assertEqual(result, node_val)
        self.assertEqual(list_ord.len(), 3)

    def test_merge_lists(self):
        list_ord = self.list
        list_ord.add(1)
        list_ord.add(2)

        lost_ord_2 = OrderedList(True)
        lost_ord_2.add(3)
        lost_ord_2.add(4)
        lost_ord_2.add(5)

        res = merge_lists(lost_ord_2, list_ord)
        result = list(map(lambda x: x.value, res.get_all()))
        node_val = [1, 2, 3, 4, 5]

        self.assertEqual(result, node_val)
        self.assertEqual(res.len(), 5)

    def test_merge_lists_False(self):
        list_ord = OrderedList(False)
        list_ord.add(1)
        list_ord.add(1)
        list_ord.add(2)

        lost_ord_2 = OrderedList(False)
        lost_ord_2.add(3)
        lost_ord_2.add(4)
        lost_ord_2.add(5)

        res = merge_lists(lost_ord_2, list_ord)
        result = list(map(lambda x: x.value, res.get_all()))
        node_val = [5,4,3,2,1,1]

        self.assertEqual(result, node_val)
        self.assertEqual(res.len(), 6)

    def test_ordered_list_with_sublist_func(self):
        lost_ord_2 = OrderedListWithSubListFunc(True)
        lost_ord_2.add(3)
        lost_ord_2.add(4)
        lost_ord_2.add(5)

        sub = OrderedListWithSubListFunc(True)
        sub.add(4)
        sub.add(5)

        res = lost_ord_2.find_sub_list(sub)

        self.assertTrue(res)

    def test_find_popular_value(self):
        lost_ord_2 = self.list
        lost_ord_2.add(3)
        lost_ord_2.add(4)
        lost_ord_2.add(4)
        lost_ord_2.add(4)
        lost_ord_2.add(4)
        lost_ord_2.add(5)
        lost_ord_2.add(5)
        lost_ord_2.add(5)

        res = find_popular_value(lost_ord_2)

        self.assertEqual(res, 4)

    def test_index_of_value(self):
        lost_ord_2 = OrderedListWithIndex(True)
        lost_ord_2.add(3)
        lost_ord_2.add(4)
        lost_ord_2.add(5)
        lost_ord_2.add(6)
        lost_ord_2.add(7)

        res = lost_ord_2.find_index(7)

        self.assertEqual(res, 4)