from django.test import TestCase
import unittest
import verify

# Create your tests here.
class TestConversor(unittest.TestCase):

    def test_convertir_diez_a_romano(self):
        self.assertEqual(verify.verificar(),'ubOEqfp9ZHP0gL4lkoYbrnaotwG3')


if __name__ == "__main__":
    unittest.main()