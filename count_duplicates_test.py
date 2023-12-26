import unittest
from count_duplicates import count_duplicates

class TestCountDuplicates(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(count_duplicates("Hello, World!"), 3)

    def test_case2(self):
        self.assertEqual(count_duplicates("Programming"), 1)

    def test_case3(self):
        self.assertEqual(count_duplicates("aabbcde"), 2)

    def test_case4(self):
        self.assertEqual(count_duplicates("12345"), 0)

if __name__ == '__main__':
    unittest.main()