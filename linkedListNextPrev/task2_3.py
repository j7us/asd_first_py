import unittest

from linkedListNextPrev.task2 import LinkedList2, Node
from linkedListNextPrev.task2_2 import reverse, is_any_loop_in_list, sort_list, combine


class LinkedList2Test(unittest.TestCase):
    def setUp(self):
        self.start_list = LinkedList2()

    def test_find_success_single_val(self):
        cur_list = self.start_list
        cur_list.add_in_tail(Node(1))

        find_node = cur_list.find(1)

        self.assertEqual(find_node.value,1)

    def test_find_success_multiple_val(self):
        cur_list = self.start_list
        cur_list.add_in_tail(Node(1))
        cur_list.add_in_tail(Node(2))
        cur_list.add_in_tail(Node(3))

        find_node = cur_list.find(3)

        self.assertEqual(find_node.value,3)

    def test_find_false(self):
        cur_list = self.start_list
        cur_list.add_in_tail(Node(1))
        cur_list.add_in_tail(Node(2))
        cur_list.add_in_tail(Node(3))

        find_node = cur_list.find(55)

        self.assertIsNone(find_node)

    def test_find_empty(self):
        cur_list = self.start_list

        find_node = cur_list.find(55)

        self.assertIsNone(find_node)

    def test_find_all_success_single_val(self):
        cur_list = self.start_list
        cur_list.add_in_tail(Node(1))

        find_list = cur_list.find_all(1)

        self.assertEqual(len(find_list),1)
        self.assertEqual(list(map(lambda x: x.value, find_list)), [1])

    def test_find_al_success_multiple_val(self):
        cur_list = self.start_list
        cur_list.add_in_tail(Node(1))
        cur_list.add_in_tail(Node(2))
        cur_list.add_in_tail(Node(1))
        cur_list.add_in_tail(Node(3))
        cur_list.add_in_tail(Node(1))

        find_list = cur_list.find_all(1)

        self.assertEqual(len(find_list),3)
        self.assertEqual(list(map(lambda x: x.value, find_list)), [1,1,1])

    def test_find_all_false(self):
        cur_list = self.start_list
        cur_list.add_in_tail(Node(1))
        cur_list.add_in_tail(Node(2))
        cur_list.add_in_tail(Node(1))
        cur_list.add_in_tail(Node(3))
        cur_list.add_in_tail(Node(1))

        find_list = cur_list.find_all(55)

        self.assertEqual(len(find_list), 0)

    def test_find_all_empty(self):
        cur_list = self.start_list

        find_list = cur_list.find_all(55)

        self.assertEqual(len(find_list), 0)

    def test_delete_one(self):
        cur_list = self.start_list
        cur_list.add_in_tail(Node(1))
        cur_list.add_in_tail(Node(2))
        cur_list.add_in_tail(Node(3))
        cur_list.add_in_tail(Node(4))
        cur_list.add_in_tail(Node(5))

        cur_list.delete(3)

        count = cur_list.len()
        deleted_node = cur_list.find(3)

        self.assertEqual(count, 4)
        self.assertIsNone(deleted_node)

    def test_delete_head(self):
        cur_list = self.start_list
        cur_list.add_in_tail(Node(1))
        cur_list.add_in_tail(Node(2))
        cur_list.add_in_tail(Node(3))
        cur_list.add_in_tail(Node(4))
        cur_list.add_in_tail(Node(5))

        cur_list.delete(1)

        count = cur_list.len()
        deleted_node = cur_list.find(1)

        self.assertEqual(count, 4)
        self.assertIsNone(deleted_node)
        self.assertEqual(cur_list.head.value, 2)
        self.assertIsNone(cur_list.head.prev)

    def test_delete_tail(self):
        cur_list = self.start_list
        cur_list.add_in_tail(Node(1))
        cur_list.add_in_tail(Node(2))
        cur_list.add_in_tail(Node(3))
        cur_list.add_in_tail(Node(4))
        cur_list.add_in_tail(Node(5))

        cur_list.delete(5)

        count = cur_list.len()
        deleted_node = cur_list.find(5)

        self.assertEqual(count, 4)
        self.assertIsNone(deleted_node)
        self.assertEqual(cur_list.tail.value, 4)
        self.assertIsNone(cur_list.tail.next)

    def test_delete_tail_and_head(self):
        cur_list = self.start_list
        cur_list.add_in_tail(Node(1))

        cur_list.delete(1)

        count = cur_list.len()
        deleted_node = cur_list.find(1)

        self.assertEqual(count, 0)
        self.assertIsNone(deleted_node)
        self.assertIsNone(cur_list.head)
        self.assertIsNone(cur_list.tail)

    def test_delete_false(self):
        cur_list = self.start_list
        cur_list.add_in_tail(Node(1))
        cur_list.add_in_tail(Node(2))
        cur_list.add_in_tail(Node(3))
        cur_list.add_in_tail(Node(4))
        cur_list.add_in_tail(Node(5))

        cur_list.delete(55)

        count = cur_list.len()

        self.assertEqual(count, 5)
        self.assertEqual(cur_list.head.value, 1)
        self.assertEqual(cur_list.tail.value, 5)

    def test_delete_empty(self):
        cur_list = self.start_list

        cur_list.delete(55, True)

        count = cur_list.len()

        self.assertEqual(count, 0)

    def test_delete_all(self):
        cur_list = self.start_list
        cur_list.add_in_tail(Node(1))
        cur_list.add_in_tail(Node(2))
        cur_list.add_in_tail(Node(1))
        cur_list.add_in_tail(Node(4))
        cur_list.add_in_tail(Node(1))

        cur_list.delete(1, True)

        count = cur_list.len()
        deleted_node = cur_list.find(1)

        self.assertEqual(count, 2)
        self.assertIsNone(deleted_node)
        self.assertEqual(cur_list.head.value, 2)
        self.assertEqual(cur_list.tail.value, 4)

    def test_insert_empty(self):
        cur_list = self.start_list

        cur_list.insert(None, Node(1))

        count = cur_list.len()
        node_in_list = cur_list.find(1)

        self.assertEqual(count, 1)
        self.assertIsNotNone(node_in_list)
        self.assertEqual(cur_list.head.value, 1)
        self.assertEqual(cur_list.tail.value, 1)

    def test_insert_in_tail(self):
        cur_list = self.start_list

        cur_list.add_in_tail(Node(1))
        cur_list.add_in_tail(Node(2))

        cur_list.insert(None, Node(3))

        count = cur_list.len()
        node_in_list = cur_list.find(3)
        second_node = cur_list.find(2)

        self.assertEqual(second_node.next.value, 3)
        self.assertEqual(count, 3)
        self.assertIsNotNone(node_in_list)
        self.assertEqual(node_in_list.prev.value, 2)
        self.assertEqual(cur_list.head.value, 1)
        self.assertEqual(cur_list.tail.value, 3)

    def test_insert_after_tail(self):
        cur_list = self.start_list

        second_node = Node(2)

        cur_list.add_in_tail(Node(1))
        cur_list.add_in_tail(second_node)

        cur_list.insert(second_node, Node(3))

        count = cur_list.len()
        node_in_list = cur_list.find(3)

        self.assertEqual(second_node.next.value, 3)
        self.assertEqual(count, 3)
        self.assertIsNotNone(node_in_list)
        self.assertEqual(node_in_list.prev.value, 2)
        self.assertEqual(cur_list.head.value, 1)
        self.assertEqual(cur_list.tail.value, 3)

    def test_insert_in_middle(self):
        cur_list = self.start_list

        second_node = Node(2)

        cur_list.add_in_tail(Node(1))
        cur_list.add_in_tail(second_node)
        cur_list.add_in_tail(Node(4))

        cur_list.insert(second_node, Node(3))

        count = cur_list.len()
        node_in_list = cur_list.find(4)

        self.assertEqual(second_node.next.value, 3)
        self.assertEqual(count, 4)
        self.assertEqual(node_in_list.prev.value, 3)
        self.assertEqual(cur_list.head.value, 1)
        self.assertEqual(cur_list.tail.value, 4)

    def test_add_in_tail_empty(self):
        cur_list = self.start_list

        cur_list.add_in_head(Node(1))

        count = cur_list.len()
        node_in_list = cur_list.find(1)

        self.assertEqual(count, 1)
        self.assertIsNotNone(node_in_list)
        self.assertEqual(cur_list.head.value, 1)
        self.assertEqual(cur_list.tail.value, 1)

    def test_add_in_tail_one(self):
        cur_list = self.start_list
        cur_list.add_in_tail(Node(1))

        cur_list.add_in_head(Node(2))

        count = cur_list.len()
        node_in_list = cur_list.find(2)

        self.assertEqual(count, 2)
        self.assertIsNotNone(node_in_list)
        self.assertEqual(cur_list.head.value, 2)
        self.assertEqual(cur_list.tail.value, 1)

    def test_add_in_tail_multiple(self):
        cur_list = self.start_list
        cur_list.add_in_tail(Node(2))
        cur_list.add_in_tail(Node(3))

        cur_list.add_in_head(Node(1))

        count = cur_list.len()
        node_in_list = cur_list.find(1)

        self.assertEqual(count, 3)
        self.assertIsNotNone(node_in_list)
        self.assertEqual(cur_list.head.value, 1)
        self.assertEqual(cur_list.tail.value, 3)

    def test_clean(self):
        cur_list = self.start_list
        cur_list.add_in_tail(Node(1))

        cur_list.clean()

        count = cur_list.len()

        self.assertEqual(count, 0)
        self.assertIsNone(cur_list.head)
        self.assertIsNone(cur_list.tail)

    def test_clean_empty(self):
        cur_list = self.start_list

        cur_list.clean()

        count = cur_list.len()

        self.assertEqual(count, 0)
        self.assertIsNone(cur_list.head)
        self.assertIsNone(cur_list.tail)

    def test_len_empty(self):
        cur_list = self.start_list

        count = cur_list.len()

        self.assertEqual(count, 0)

    def test_len(self):
        cur_list = self.start_list
        cur_list.add_in_tail(Node(1))
        cur_list.add_in_tail(Node(1))
        cur_list.add_in_tail(Node(1))
        cur_list.add_in_tail(Node(1))

        node_after = Node(1)

        cur_list.insert(None, node_after)

        cur_list.add_in_tail(Node(1))

        cur_list.insert(node_after, Node(1))

        cur_list.delete(1)

        count = cur_list.len()

        self.assertEqual(count, 6)

    def test_revers(self):
        cur_list = self.start_list
        cur_list.add_in_tail(Node(1))
        cur_list.add_in_tail(Node(2))
        cur_list.add_in_tail(Node(3))
        cur_list.add_in_tail(Node(4))

        reverse(cur_list)

        count = cur_list.len()

        self.assertEqual(count, 4)
        self.assertEqual(cur_list.head.value, 4)
        self.assertEqual(cur_list.tail.value, 1)

    def test_is_any_loop_in_list(self):
        cur_list = self.start_list

        cur_list.add_in_tail(Node(1))
        cur_list.add_in_tail(Node(2))
        cur_list.add_in_tail(Node(3))
        cur_list.add_in_tail(Node(4))

        cur_list.tail.next = cur_list.head
        cur_list.head.prev = cur_list.tail

        res = is_any_loop_in_list(cur_list)

        self.assertTrue(res)

    def test_is_any_loop_in_list_false(self):
        cur_list = self.start_list

        cur_list.add_in_tail(Node(1))
        cur_list.add_in_tail(Node(2))
        cur_list.add_in_tail(Node(3))
        cur_list.add_in_tail(Node(4))

        res = is_any_loop_in_list(cur_list)

        self.assertFalse(res)

    def test_sort(self):
        cur_list = self.start_list

        cur_list.add_in_tail(Node(3))
        cur_list.add_in_tail(Node(2))
        cur_list.add_in_tail(Node(142))
        cur_list.add_in_tail(Node(223))
        cur_list.add_in_tail(Node(24))
        cur_list.add_in_tail(Node(255))
        cur_list.add_in_tail(Node(21))

        sort_list(cur_list)

        count = cur_list.len()

        self.assertEqual(count, 7)
        self.assertEqual(cur_list.head.value, 2)
        self.assertEqual(cur_list.tail.value, 255)

    def test_combine(self):
        cur_list = self.start_list

        cur_list.add_in_tail(Node(3))
        cur_list.add_in_tail(Node(2))
        cur_list.add_in_tail(Node(142))
        cur_list.add_in_tail(Node(223))

        second_cur_list = LinkedList2()

        second_cur_list.add_in_tail(Node(2123))
        second_cur_list.add_in_tail(Node(3))
        second_cur_list.add_in_tail(Node(414))

        result = combine(second_cur_list, cur_list)

        count = result.len()

        self.assertEqual(count, 7)
        self.assertEqual(result.head.value, 2)
        self.assertEqual(result.tail.value, 2123)