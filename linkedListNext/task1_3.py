import unittest

from linkedListNext.task1_2 import list_sum
from linkedListNext.task1 import LinkedList, Node


class LinkedListTest(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_delete_one_node(self):
        list = self.linked_list
        list.add_in_tail(Node(1))

        list.delete(1)
        node = list.find(1)

        self.assertIsNone(node)

    def test_delete_all_nodes(self):
        list = self.linked_list
        list.add_in_tail(Node(1))
        list.add_in_tail(Node(1))

        list.delete(1, True)

        node = list.find(1)
        self.assertIsNone(node)

    def test_delete_node_and_check_new_head(self):
        list = self.linked_list
        list.add_in_tail(Node(1))
        list.add_in_tail(Node(2))

        list.delete(1, True)

        second_node = list.find(2)
        deleting_node = list.find(1)

        self.assertEqual(list.head.value, 2)
        self.assertIsNone(deleting_node)
        self.assertEqual(second_node.value, 2)

    def test_delete_node_and_check_second(self):
        list = self.linked_list
        list.add_in_tail(Node(1))
        list.add_in_tail(Node(2))
        list.add_in_tail(Node(3))

        list.delete(1)

        head_node = list.find(2)
        second_node = list.find(3)
        deleting_node = list.find(1)


        self.assertIsNone(deleting_node)
        self.assertEqual(head_node.value, 2)
        self.assertEqual(second_node.value, 3)

    def test_delete_none(self):
        list = self.linked_list
        list.add_in_tail(Node(1))

        list.delete(5)

        node = list.find(1)
        self.assertEqual(node.value, 1)

    def test_clean(self):
        list = self.linked_list
        list.add_in_tail(Node(1))

        list.clean()

        node = list.find(1)
        self.assertIsNone(node)

    def test_len(self):
        list = self.linked_list
        list.add_in_tail(Node(1))

        counter = list.len()
        self.assertEqual(counter, 1)

    def test_len_multiple(self):
        list = self.linked_list
        list.add_in_tail(Node(1))
        list.add_in_tail(Node(2))
        list.add_in_tail(Node(3))

        counter = list.len()
        self.assertEqual(counter, 3)

    def test_len_empty(self):
        list = self.linked_list

        counter = list.len()
        self.assertEqual(counter, 0)

    def test_len_insert_delete(self):
        list = self.linked_list

        first_node = Node(1)

        list.add_in_tail(first_node)
        list.add_in_tail(Node(2))
        list.add_in_tail(Node(2))
        list.add_in_tail(Node(2))
        list.add_in_tail(Node(3))
        list.add_in_tail(Node(3))
        list.add_in_tail(Node(3))

        list.delete(2)
        list.delete(3, True)
        list.insert(None, Node(4))
        list.insert(first_node, Node(5))

        counter = list.len()

        self.assertEqual(counter, 5)

    def test_insert_head(self):
        list = self.linked_list
        first_node = Node(1)

        list.add_in_tail(first_node)
        list.add_in_tail(Node(2))
        list.add_in_tail(Node(3))

        node_to_insert = Node(4)
        list.insert(None, node_to_insert)

        new_head = list.find(4)
        print(list.head.value)
        self.assertEqual(list.head, node_to_insert)
        self.assertEqual(new_head.next, first_node)

    def test_insert_after(self):
        list = self.linked_list
        first_node = Node(1)
        second_node = Node(2)

        list.add_in_tail(first_node)
        list.add_in_tail(second_node)
        list.add_in_tail(Node(3))

        node_to_insert = Node(4)
        list.insert(first_node, node_to_insert)


        self.assertEqual(first_node.next, node_to_insert)
        self.assertEqual(node_to_insert.next, second_node)

    def test_find_all(self):
        list = self.linked_list
        list.add_in_tail(Node(1))
        list.add_in_tail(Node(2))
        list.add_in_tail(Node(1))

        result = list.find_all(1)
        self.assertEqual(len(result), 2)

    def test_find_all_empty(self):
        list = self.linked_list

        result = list.find_all(1)
        self.assertEqual(len(result), 0)

    def test_find_all_not_value(self):
        list = self.linked_list
        list.add_in_tail(Node(1))
        list.add_in_tail(Node(2))
        list.add_in_tail(Node(1))

        result = list.find_all(3)
        self.assertEqual(len(result), 0)

    def test_list_sum(self):
        list_first = LinkedList()
        list_first.add_in_tail(Node(1))
        list_first.add_in_tail(Node(2))
        list_first.add_in_tail(Node(3))

        list_second = LinkedList()
        list_second.add_in_tail(Node(1))
        list_second.add_in_tail(Node(2))
        list_second.add_in_tail(Node(3))

        result_list = list_sum(list_first, list_second)

        self.assertEqual(result_list.len(), 3)
        self.assertEqual(result_list.head.value, 2)

    def test_list_sum_empty(self):
        list_first = LinkedList()
        list_second = LinkedList()

        result_list = list_sum(list_first, list_second)

        self.assertEqual(result_list.len(), 0)

    def test_list_sum_diff_len(self):
        list_first = LinkedList()
        list_first.add_in_tail(Node(3))

        list_second = LinkedList()

        result_list = list_sum(list_first, list_second)

        self.assertEqual(result_list.len(), 0)

