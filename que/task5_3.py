import unittest
from que.task5 import Queue
from que.task5_2 import queue_rotation, StacksQueue, reverse_queue

class QueuTest(unittest.TestCase):
    def setUp(self):
        self.q = Queue()
        self.sq = StacksQueue()

    def test_size_empty(self):
        self.assertEqual(self.q.size(), 0)

    def test_size_one(self):
        self.q.enqueue(1)
        self.assertEqual(self.q.size(), 1)

    def test_size_multiple(self):
        self.q.enqueue(1)
        self.q.enqueue(1)
        self.q.enqueue(1)
        self.assertEqual(self.q.size(), 3)

    def test_enqueue(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)
        self.assertEqual(self.q.buffer[0], 3)
        self.assertEqual(self.q.buffer[1], 2)
        self.assertEqual(self.q.buffer[2], 1)
        self.assertEqual(self.q.size(), 3)

    def test_dequeue_empty(self):
        res = self.q.dequeue()

        self.assertIsNone(res)
        self.assertEqual(self.q.size(), 0)

    def test_dequeue_one(self):
        self.q.enqueue(3)
        res = self.q.dequeue()

        self.assertEqual(res, 3)
        self.assertEqual(len(self.q.buffer), 0)
        self.assertEqual(self.q.size(), 0)

    def test_dequeue_multiple(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)


        res_f = self.q.dequeue()
        res_s = self.q.dequeue()
        res_t = self.q.dequeue()

        self.assertEqual(res_f, 1)
        self.assertEqual(res_s, 2)
        self.assertEqual(res_t, 3)
        self.assertEqual(len(self.q.buffer), 0)
        self.assertEqual(self.q.size(), 0)

    def test_queue_rotation_not_rotate(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)
        self.q.enqueue(4)
        self.q.enqueue(5)

        queue_rotation(self.q, 0)

        self.assertEqual(self.q.buffer[4], 1)
        self.assertEqual(self.q.buffer[0], 5)
        self.assertEqual(len(self.q.buffer), 5)

    def test_queue_rotation_rotate_two(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)
        self.q.enqueue(4)
        self.q.enqueue(5)

        queue_rotation(self.q, 2)

        self.assertEqual(self.q.buffer[4], 3)
        self.assertEqual(self.q.buffer[0], 2)
        self.assertEqual(len(self.q.buffer), 5)

    def test_queue_rotation_rotate_more_than_len(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)
        self.q.enqueue(4)
        self.q.enqueue(5)

        queue_rotation(self.q, 8)

        self.assertEqual(self.q.buffer[4], 4)
        self.assertEqual(self.q.buffer[0], 3)
        self.assertEqual(len(self.q.buffer), 5)

    def test_sq_size_empty(self):
        self.assertEqual(self.sq.size(), 0)

    def test_sq_size_one(self):
        self.sq.enqueue(1)
        self.assertEqual(self.sq.size(), 1)

    def test_sq_size_multiple(self):
        self.sq.enqueue(1)
        self.sq.enqueue(1)
        self.sq.enqueue(1)
        self.assertEqual(self.sq.size(), 3)

    def test_sq_enqueue(self):
        self.sq.enqueue(1)
        self.sq.enqueue(2)
        self.sq.enqueue(3)
        self.assertEqual(self.sq.size(), 3)

    def test_sq_dequeue_empty(self):
        res = self.sq.dequeue()

        self.assertIsNone(res)
        self.assertEqual(self.sq.size(), 0)

    def test_sq_dequeue_one(self):
        self.sq.enqueue(3)
        res = self.sq.dequeue()

        self.assertEqual(res, 3)
        self.assertEqual(self.sq.size(), 0)

    def test_sq_dequeue_multiple(self):
        self.sq.enqueue(1)
        self.sq.enqueue(2)
        self.sq.enqueue(3)


        res_f = self.sq.dequeue()
        res_s = self.sq.dequeue()
        res_t = self.sq.dequeue()

        self.assertEqual(res_f, 1)
        self.assertEqual(res_s, 2)
        self.assertEqual(res_t, 3)
        self.assertEqual(self.sq.size(), 0)

    def test_reverse_queue(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)
        self.q.enqueue(4)
        self.q.enqueue(5)

        reverse_queue(self.q, )

        self.assertEqual(self.q.buffer[4], 5)
        self.assertEqual(self.q.buffer[0], 1)
        self.assertEqual(len(self.q.buffer), 5)

