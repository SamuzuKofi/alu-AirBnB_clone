#!/usr/bin/python3
import unittest
from models.base_model import add,subtract,multiply,divide,modulus


class TestBaseModel(unittest.TestCase):
    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = multiply(2, 3)
        self.assertEqual(result, 6)

    def test_divide(self):
        result = divide(6, 3)
        self.assertEqual(result, 2)

    def test_modulus(self):
        result = modulus(5, 3)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()