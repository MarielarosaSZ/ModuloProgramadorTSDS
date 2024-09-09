import unittest
from moto import Moto

class TestMoto(unittest.TestCase):

    def setUp(self):
        self.moto = Moto()

    def test_acelerar(self):
        self.moto.acelerar()
        self.assertEqual(self.moto.velocidad, 10)

    def test_frenar(self):
        self.moto.acelerar()
        self.moto.frenar()
        self.assertEqual(self.moto.velocidad, 0)

    def test_cambiar_marcha(self):
        self.moto.cambiar_marcha(2)
        self.assertEqual(self.moto.marcha, 2)

    def test_marcha_invalida(self):
        with self.assertRaises(ValueError):
            self.moto.cambiar_marcha(6)

if __name__ == '__main__':
    unittest.main()
