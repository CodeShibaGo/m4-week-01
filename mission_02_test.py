import unittest
from mission_02 import is_even

class TestIsEvenFunction(unittest.TestCase):

    def test_even_number(self):
        self.assertTrue(is_even(4))

    def test_odd_number(self):
        self.assertFalse(is_even(7))

if __name__ == '__main__':
    unittest.main()