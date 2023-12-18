import unittest
from mission_01 import add

class TestAddition(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()


def test_add_negative_numbers():
    assert add(-1, 1) == 0
