import unittest
from count_digit import nb_dig

class TestNbDig(unittest.TestCase):

    def test_nb_dig_1(self):
        self.assertEqual(nb_dig(10, 1), 4)

    def test_nb_dig_2(self):
        self.assertEqual(nb_dig(25, 1), 11)

    def test_nb_dig_3(self):
        self.assertEqual(nb_dig(1, 0), 1)

    def test_nb_dig_4(self):
        self.assertEqual(nb_dig(100, 0), 11)

    def test_nb_dig_5(self):
        self.assertEqual(nb_dig(1111, 1), 249)

if __name__ == '__main__':
    unittest.main()