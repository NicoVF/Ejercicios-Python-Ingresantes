import unittest
from Ejercicio1 import square_digits1, square_digits2, square_digits3,square_digits4


class SquareDigits1(unittest.TestCase):
    def test_123(self):
        self.assertEqual(square_digits1(123), 149)  # add assertion here

    def test_0(self):
        self.assertEqual(square_digits1(0), 0)  # add assertion here

    def test_4(self):
        self.assertEqual(square_digits1(4), 16)  # add assertion here

    def test_10(self):
        self.assertEqual(square_digits1(10), 10)  # add assertion here

    def test_12(self):
        self.assertEqual(square_digits1(12), 14)  # add assertion here

    def test_105(self):
        self.assertEqual(square_digits1(105), 1025)  # add assertion here

    def test_1000(self):
        self.assertEqual(square_digits1(1000), 1000)  # add assertion here

    def test_1025(self):
        self.assertEqual(square_digits1(1025), 10425)  # add assertion here

    def test_1222(self):
        self.assertEqual(square_digits1(1222), 1444)  # add assertion here



class SquareDigits2(unittest.TestCase):
    def test_123(self):
        self.assertEqual(square_digits2(123), 149)  # add assertion here

    def test_0(self):
        self.assertEqual(square_digits2(0), 0)  # add assertion here

    def test_4(self):
        self.assertEqual(square_digits2(4), 16)  # add assertion here

    def test_10(self):
        self.assertEqual(square_digits2(10), 10)  # add assertion here

    def test_12(self):
        self.assertEqual(square_digits2(12), 14)  # add assertion here

    def test_105(self):
        self.assertEqual(square_digits2(105), 1025)  # add assertion here

    def test_1000(self):
        self.assertEqual(square_digits2(1000), 1000)  # add assertion here

    def test_1025(self):
        self.assertEqual(square_digits2(1025), 10425)  # add assertion here

    def test_1222(self):
        self.assertEqual(square_digits2(1222), 1444)  # add assertion here


class SquareDigits3(unittest.TestCase):
    def test_123(self):
        self.assertEqual(square_digits3(123), 149)  # add assertion here

    def test_0(self):
        self.assertEqual(square_digits3(0), 0)  # add assertion here

    def test_4(self):
        self.assertEqual(square_digits3(4), 16)  # add assertion here
    def test_10(self):
        self.assertEqual(square_digits3(10), 10)  # add assertion here

    def test_12(self):
        self.assertEqual(square_digits3(12), 14)  # add assertion here

    def test_105(self):
        self.assertEqual(square_digits3(105), 1025)  # add assertion here

    def test_1000(self):
        self.assertEqual(square_digits3(1000), 1000)  # add assertion here

    def test_1025(self):
        self.assertEqual(square_digits3(1025), 10425)  # add assertion here

    def test_1222(self):
        self.assertEqual(square_digits3(1222), 1444)  # add assertion here



