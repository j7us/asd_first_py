import unittest

from dynArray.task3 import DynArray
from dynArray.task3_2 import MultiDynArray


class DynArrayTest(unittest.TestCase):
    def setUp(self):
        self.dyn_array = DynArray()

    def test_insert_last(self):
        array = self.dyn_array

        array.append(1)
        array.append(2)
        array.append(3)
        array.append(4)
        array.append(5)

        array.insert(5, 6)

        res = array[5]

        self.assertEqual(res, 6)
        self.assertEqual(len(array), 6)
        self.assertEqual(array.capacity, 16)

    def test_insert_first(self):
        array = self.dyn_array

        array.insert(0, 6)

        res = array[0]

        self.assertEqual(res, 6)
        self.assertEqual(len(array), 1)
        self.assertEqual(array.capacity, 16)

    def test_insert_middle(self):
        array = self.dyn_array

        array.append(1)
        array.append(2)
        array.append(3)
        array.append(4)
        array.append(5)

        array.insert(1, 6)

        res = array[1]

        self.assertEqual(res, 6)
        self.assertEqual(len(array), 6)
        self.assertEqual(array.capacity, 16)

    def test_insert_exception(self):
        array = self.dyn_array

        array.append(1)
        array.append(2)
        array.append(3)
        array.append(4)
        array.append(5)

        exc_throws = False
        try:
            array.insert(6, 6)
        except IndexError:
            exc_throws = True

        self.assertTrue(exc_throws)
        self.assertEqual(len(array), 5)
        self.assertEqual(array.capacity, 16)

    def test_insert_with_cap(self):
        array = self.dyn_array

        for i in range(16):
            array.append(i)

        array.insert(1, 17)

        res = array[1]

        self.assertEqual(res, 17)
        self.assertEqual(len(array), 17)
        self.assertEqual(array.capacity, 32)

    def test_delete_first(self):
        array = self.dyn_array

        for i in range(7):
            array.append(i)

        array.delete(0)

        res = array[3]

        self.assertEqual(res, 4)
        self.assertIsNone(array.array[6])
        self.assertEqual(len(array), 6)
        self.assertEqual(array.capacity, 16)

    def test_delete_last(self):
        array = self.dyn_array

        for i in range(10):
            array.append(i)

        array.delete(9)

        no_element = False
        try:
            array[9]
        except IndexError:
            no_element = True

        self.assertTrue(no_element)
        self.assertEqual(len(array), 9)
        self.assertEqual(array.capacity, 16)

    def test_delete_index_err(self):
        array = self.dyn_array

        for i in range(10):
            array.append(i)

        err = False
        try:
            array.delete(10)
        except IndexError:
            err = True

        self.assertTrue(err)
        self.assertEqual(len(array), 10)
        self.assertEqual(array.capacity, 16)

    def test_delete_resize_default(self):
        array = self.dyn_array

        for i in range(8):
            array.append(i)

        array.delete(5)

        res = array[5]

        self.assertEqual(res, 6)
        self.assertEqual(len(array), 7)
        self.assertEqual(array.capacity, 16)

    def test_delete_resize(self):
        array = self.dyn_array

        for i in range(33):
            array.append(i)

        array.delete(0)
        array.delete(0)

        res = array[0]

        self.assertEqual(res, 2)
        self.assertEqual(len(array), 31)
        self.assertEqual(array.capacity, 42)

