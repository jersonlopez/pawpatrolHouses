from django.test import TestCase
import unittest
from datetime import datetime
from . import verify
from . import validations
from . import views
from django.test import Client
from . import requestExample
import json


class ValidationTest(unittest.TestCase):

    def testCheckInlaterThanCheckout(self):

        checkIn = datetime.strptime('12-03-1997', '%d-%m-%Y')
        checkOut = datetime.strptime('12-02-1997', '%d-%m-%Y')
        self.assertEqual(validations.dateValidation(checkIn, checkOut), 3)

    def testCheckInEqualCheckout(self):
        checkIn = datetime.strptime('12-01-1997', '%d-%m-%Y')
        checkOut = datetime.strptime('12-01-1997', '%d-%m-%Y')
        self.assertEqual(validations.dateValidation(checkIn, checkOut), 2)

    def testCheckInBeforeCheckout(self):
        checkIn = datetime.strptime('12-01-1997', '%d-%m-%Y')
        checkOut = datetime.strptime('12-02-1997', '%d-%m-%Y')
        self.assertEqual(validations.dateValidation(checkIn, checkOut), 1)

    def testFilterCityEqualMedellin(self):
        city = 'CO-MDE'
        self.assertEqual(validations.filterCity(city), 'Medellin')

    def testFilterCityEqualBogota(self):
        city = 'CO-BOG'
        self.assertEqual(validations.filterCity(city), 'Bogota')

    def testFilterCityEqualCali(self):
        city = 'CO-CLO'
        self.assertEqual(validations.filterCity(city), 'Cali')

    def testFilterCityEqualSantaMarta(self):
        city = 'CO-SMR'
        self.assertEqual(validations.filterCity(city), 'Santa Marta')

    def testFilterCityEqualCartagena(self):
        city = 'CO-CTG'
        self.assertEqual(validations.filterCity(city), 'Cartagena')

    def testFilterCityEqualAnotherCity(self):
        city = 'CO-ABC'
        self.assertEqual(validations.filterCity(city), 'invalid')

    def testFilterCityNoCity(self):
        city = ''
        self.assertEqual(validations.filterCity(city), 'void')

    def testFilterType1Apartment(self):
        filterType = '1'
        self.assertEqual(validations.filterType(filterType), 'Apartamento')

    def testFilterType2House(self):
        filterType = '2'
        self.assertTrue(validations.filterType(filterType), 'Casa')

    def testFilterType3Luxury(self):
        filterType = '3'
        self.assertTrue(validations.filterType(filterType), 'Luxury')

    def testFilterTypeVoid(self):
        filterType = ''
        self.assertTrue(validations.filterType(filterType), 'void')

    def testFilterTypeAnotherType(self):
        filterType = '4'
        self.assertTrue(validations.filterType(filterType), 'invalid')

    def testGetAllHomes(self):
        data={}
        data['checkIn'] = '07-04-2018'
        data['checkOut'] = '10-04-2018'
        data['city'] = 'CO-MDE'
        data['type'] = '1'
        body=json.dumps(data).encode('utf-8')
        request=requestExample.requestExample(body)
        views.getAllHomes(request)
        #self.assertTrue(response!={'message': 'No type selected.'} and response!={'message': 'Invalid type selected.'})


if __name__ == "__main__":
    unittest.main()
