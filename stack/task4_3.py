import unittest

from stack.task4 import Stack
from stack.task4_2 import validate_staples, validate_staples_with_different_type, calculate_with_postfix


class StackTest(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_one_element(self):
        self.stack.push(1)

        self.assertEqual(self.stack.size(), 1)
        self.assertEqual(self.stack.stack[0], 1)

    def test_push_multiple_element(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)

        self.assertEqual(self.stack.size(), 4)
        self.assertEqual(self.stack.stack[0], 4)

    def test_peek_with_elements(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)

        peek_res = self.stack.peek()

        self.assertEqual(self.stack.size(), 4)
        self.assertEqual(peek_res, 4)

    def test_peek_empty(self):
        peek_res = self.stack.peek()

        self.assertEqual(self.stack.size(), 0)
        self.assertIsNone(peek_res)

    def test_pop_empty(self):
        pop_res = self.stack.pop()

        self.assertEqual(self.stack.size(), 0)
        self.assertIsNone(pop_res)

    def test_pop_with_one_elements(self):
        self.stack.push(1)

        pop_res = self.stack.pop()

        self.assertEqual(self.stack.size(), 0)
        self.assertEqual(pop_res, 1)

    def test_pop_with_multiple_elements(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)

        pop_res_1 = self.stack.pop()
        pop_res_2 = self.stack.pop()
        pop_res_3 = self.stack.pop()
        pop_res_4 = self.stack.pop()
        pop_res_5 = self.stack.pop()

        self.assertEqual(pop_res_1, 4)
        self.assertEqual(pop_res_2, 3)
        self.assertEqual(pop_res_3, 2)
        self.assertEqual(pop_res_4, 1)
        self.assertIsNone(pop_res_5)
        self.assertEqual(self.stack.size(), 0)

    def test_validate_staples_false_close(self):
        self.assertFalse(validate_staples('()))'))

    def test_validate_staples_false_open(self):
        self.assertFalse(validate_staples('())('))

    def test_validate_staples_true(self):
        self.assertTrue(validate_staples('(((()())))'))

    def test_validate_staples_with_different_type_false_close(self):
        self.assertFalse(validate_staples_with_different_type('()}'))

    def test_validate_staples_with_different_type_false_open(self):
        self.assertFalse(validate_staples_with_different_type('()[}'))

    def test_validate_staples_with_different_type_true(self):
        self.assertTrue(validate_staples_with_different_type('{}[(){}{()[()]}]'))

    def test_calculate_with_postfix(self):
        self.assertEqual(calculate_with_postfix('8 2 + 5 * 9 + ='), 59)

