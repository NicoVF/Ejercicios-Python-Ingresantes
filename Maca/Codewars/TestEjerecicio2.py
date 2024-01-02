import unittest
from Ejercicio2 import create_phone_number2


class NumeroTelefono(unittest.TestCase):
    def test_3456789873(self):
        self.assertEqual(create_phone_number2(3456789873), "(345) 678-9873")  # add assertion here

    def test_1005678990(self):
        self.assertEqual(create_phone_number2(1005678990), "(100) 567-8990")  # add assertion here

    def test_2310001231(self):
        self.assertEqual(create_phone_number2(2310001231), "(231) 000-1231")  # add assertion here

    def test_3456137843(self):
        self.assertEqual(create_phone_number2(3456137843), "(345) 613-7843")  # add assertion here
