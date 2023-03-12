import unittest
from fibonacci_number_recursive_v1 import derive_fibonacci_number

class TestRecursiveFibonacci(unittest.TestCase):
    def test_derive_first_fn(self):
        product = derive_fibonacci_number(1)
        self.assertEqual(product, 1)

    def test_derive_second_fn(self):
        product = derive_fibonacci_number(2)
        self.assertEqual(product, 1)

    def test_derive_third_fn(self):
        product = derive_fibonacci_number(3)
        self.assertEqual(product, 2)

    def test_derive_nineteenth_fn(self):
        product = derive_fibonacci_number(19)
        self.assertEqual(product, 4181)

if __name__ == '__main__':
    unittest.main()