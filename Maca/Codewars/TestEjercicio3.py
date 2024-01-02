import unittest
from Ejercicio3 import is_square

class TestSquare(unittest.TestCase):
    def test_neg1(self):
        self.assertEqual(is_square(-1), False)  # add assertion here

    def test_0(self):
        self.assertEqual(is_square(0), True)  # add assertion here

    def test_1(self):
        self.assertEqual(is_square(1), True)  # add assertion here

    def test_2(self):
        self.assertEqual(is_square(2), False)  # add assertion here

    def test_3(self):
        self.assertEqual(is_square(3), False)  # add assertion here

    def test_4(self):
        self.assertEqual(is_square(4), True)  # add assertion here

    def test_8(self):
        self.assertEqual(is_square(8), False)  # add assertion here

    def test_12(self):
        self.assertEqual(is_square(12), False)  # add assertion here

    def test_100(self):
        self.assertEqual(is_square(100), True)  # add assertion here

    def test_144(self):
        self.assertEqual(is_square(144), True)  # add assertion here

    def test_215(self):
        self.assertFalse(is_square(215), "Error 215 no tiene raiz cuadrada entera")  # add assertion here

    def test_1000(self):
        self.assertFalse(is_square(1000), "Error 1000 no tiene raiz cuadrada entera")  # add assertion here
