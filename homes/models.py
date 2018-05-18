from django.db import models
import datetime

# Create your models here.
class Location(models.Model):
    address = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=10, decimal_places=8)

    def _str_(self):              
        return self.address

class Agency(models.Model):
    name = models.CharField(max_length=200)
    nit = models.CharField(max_length=200)

    def _str_(self):              
        return self.name

class Homes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    pricePerNight = models.DecimalField(max_digits=10, decimal_places=2)
    thumbnail = models.CharField(max_length=200)

    def _str_(self):              
        return self.name

class Booking(models.Model):
    checkIn = models.DateTimeField('check in')
    checkOut = models.DateTimeField('check out')
    bookingId = models.IntegerField(primary_key=True)
    homeId = models.ForeignKey(Homes, on_delete=models.CASCADE)

    def _str_(self):
        return self.bookingId

    @classmethod
    def addBooking(cls, checkIn, checkOut, homeId):
        booking = cls(checkIn=checkIn,checkOut=checkOut,) 
        return booking
