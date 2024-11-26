# python -m unittest discover -s test_kolok
import unittest
from kolok import get_fibonacci


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_sequence(self):
        self.assertEqual(get_fibonacci(1), [0])
        self.assertEqual(get_fibonacci(2), [0, 1])
        self.assertEqual(get_fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(get_fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            get_fibonacci(0)
        with self.assertRaises(ValueError):
            get_fibonacci(-5)
        with self.assertRaises(ValueError):
            get_fibonacci("ten")


if __name__ == "__main__":
    unittest.main()