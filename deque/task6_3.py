import unittest

from deque.task6 import Deque
from deque.task6_2 import is_palindrome, DequeWithMin


class QueuTest(unittest.TestCase):
    def setUp(self):
        self.q = Deque()
        self.q_min = DequeWithMin()

    def test_size_empty(self):
        self.assertEqual(self.q.size(), 0)

    def test_size_one(self):
        self.q.addTail(1)
        self.assertEqual(self.q.size(), 1)

    def test_size_multiple(self):
        self.q.addFront(1)
        self.q.addTail(1)
        self.q.addFront(1)
        self.assertEqual(self.q.size(), 3)

    def test_add_front(self):
        self.q.addFront(1)
        self.q.addFront(2)
        self.q.addFront(3)
        self.assertEqual(self.q.buffer[0], 1)
        self.assertEqual(self.q.buffer[1], 2)
        self.assertEqual(self.q.buffer[2], 3)
        self.assertEqual(self.q.size(), 3)

    def test_add_tail(self):
        self.q.addTail(1)
        self.q.addTail(2)
        self.q.addTail(3)
        self.assertEqual(self.q.buffer[0], 3)
        self.assertEqual(self.q.buffer[1], 2)
        self.assertEqual(self.q.buffer[2], 1)
        self.assertEqual(self.q.size(), 3)


    def test_add_tail_add_front(self):
        self.q.addTail(1)
        self.q.addTail(2)
        self.q.addTail(3)
        self.q.addFront(4)
        self.q.addFront(5)
        self.assertEqual(self.q.buffer[0], 3)
        self.assertEqual(self.q.buffer[1], 2)
        self.assertEqual(self.q.buffer[2], 1)
        self.assertEqual(self.q.buffer[3], 4)
        self.assertEqual(self.q.buffer[4], 5)
        self.assertEqual(self.q.size(), 5)

    def test_remove_front_empty(self):
        res = self.q.removeFront()

        self.assertIsNone(res)
        self.assertEqual(self.q.size(), 0)

    def test_remove_tail_empty(self):
        res = self.q.removeTail()

        self.assertIsNone(res)
        self.assertEqual(self.q.size(), 0)

    def test_remove_front_one(self):
        self.q.addFront(3)
        res = self.q.removeFront()

        self.assertEqual(res, 3)
        self.assertEqual(len(self.q.buffer), 0)
        self.assertEqual(self.q.size(), 0)

    def test_remove_tail_one(self):
        self.q.addFront(3)
        res = self.q.removeTail()

        self.assertEqual(res, 3)
        self.assertEqual(len(self.q.buffer), 0)
        self.assertEqual(self.q.size(), 0)

    def test_delete_multiple(self):
        self.q.addTail(1)
        self.q.addTail(2)
        self.q.addTail(3)


        res_f = self.q.removeTail()
        res_s = self.q.removeFront()

        self.assertEqual(res_f, 3)
        self.assertEqual(res_s, 1)
        self.assertEqual(len(self.q.buffer), 1)
        self.assertEqual(self.q.size(), 1)

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome('aabcaa'))

    def test_is_palindrome_one(self):
        self.assertTrue(is_palindrome('a'))

    def test_is_palindrome_true(self):
        self.assertTrue(is_palindrome('abcddcba'))

    def test_min_empty(self):
        self.assertIsNone(self.q_min.min())

    def test_min(self):
        self.q_min.addTail(1)
        self.q_min.addTail(2)

        self.assertEqual(self.q_min.min(), 1)

    def test_min_tail_front(self):
        self.q_min.addTail(2)
        self.q_min.addTail(1)
        self.q_min.addFront(0)
        self.q_min.addFront(5)

        self.q_min.removeTail()
        self.q_min.removeTail()

        self.assertEqual(self.q_min.min(), 0)

