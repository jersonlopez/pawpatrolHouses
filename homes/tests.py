from django.test import TestCase
import unittest
from datetime import datetime 
from . import verify
from . import validations

# Create your tests here.
#class TestConversor(unittest.TestCase):

   # def test_convertir_diez_a_romano(self):
   #     self.assertEqual(verify.verificar(),'ubOEqfp9ZHP0gL4lkoYbrnaotwG3')


class ValidationTest(unittest.TestCase):

    def testCheckInlaterThanCheckout(self):

        checkIn = datetime.strptime('12-03-1997','%d-%m-%Y')
        checkOut = datetime.strptime('12-02-1997','%d-%m-%Y')
        self.assertEqual(validations.dateValidation(checkIn,checkOut),3)
    
    def testCheckInEqualCheckout(self):
        checkIn = datetime.strptime('12-01-1997','%d-%m-%Y')
        checkOut = datetime.strptime('12-01-1997','%d-%m-%Y')
        self.assertEqual(validations.dateValidation(checkIn,checkOut),2)

    def testCheckInBeforeCheckout(self):
        checkIn = datetime.strptime('12-01-1997','%d-%m-%Y')
        checkOut = datetime.strptime('12-02-1997','%d-%m-%Y')
        self.assertEqual(validations.dateValidation(checkIn,checkOut),1)

    def testFilterCityEqualMedellin(self):
        city='CO-MDE'
        self.assertEqual(validations.filterCity(city),'Medellin')
    
    def testFilterCityEqualBogota(self):
        city='CO-BOG'
        self.assertEqual(validations.filterCity(city),'Bogota')
    
    def testFilterCityEqualCali(self):
        city='CO-CLO'
        self.assertEqual(validations.filterCity(city),'Cali')

    def testFilterCityEqualSantaMarta(self):
        city='CO-SMR'
        self.assertEqual(validations.filterCity(city),'Santa Marta')

    def testFilterCityEqualCartagena(self):
        city='CO-CTG'
        self.assertEqual(validations.filterCity(city),'Cartagena')

    def testFilterCityEqualAnotherCity(self):
        city='CO-ABC'
        self.assertEqual(validations.filterCity(city),'invalid')

    def testFilterCityNoCity(self):
        city=''
        self.assertEqual(validations.filterCity(city),'void')
    
    def testFilterType1Apartment(self):
        filterType='1'
        self.assertEqual(validations.filterType(filterType),'Apartamento')

    def testFilterType2House(self):
        filterType='2'
        self.assertTrue(validations.filterType(filterType),'Casa')

    def testFilterType3Luxury(self):
        filterType='3'
        self.assertTrue(validations.filterType(filterType),'Luxury')
    
    def testFilterTypeVoid(self):
        filterType=''
        self.assertTrue(validations.filterType(filterType),'void')

    def testFilterTypeAnotherType(self):
        filterType='4'
        self.assertTrue(validations.filterType(filterType),'invalid')


if __name__ == "__main__":
    unittest.main()

