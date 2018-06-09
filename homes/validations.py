from django.views.decorators.csrf import csrf_exempt
from .models import Booking
import pytz

utc=pytz.UTC

def dateValidation(checkIn, checkOut):
    if(checkOut>checkIn):
        return 1
    if(checkIn==checkOut):
        return 2
    return 3

def filterCity(city):
    if(city=="CO-MDE"):
        filterCity = 'Medellin'
    elif(city=="CO-BOG"):
        filterCity = 'Bogota'
    elif(city=="CO-CLO"):
        filterCity = 'Cali'
    elif(city=="CO-SMR"):
        filterCity = 'Santa Marta'
    elif(city=="CO-CTG"):
        filterCity = 'Cartagena'
    elif(city==""):
        filterCity = 'void'
    else:
        filterCity = 'invalid'
    return filterCity

def filterType(type):
    if(type=="1"):
        filterType = "Apartamento"
    elif(type=="2"):
        filterType = "Casa"
    elif(type=="3"):
        filterType = "Luxury"
    elif(type==""):
        filterType = "void"
    else:
        filterType = "invalid"
    return filterType

@csrf_exempt
def isHomeDisponible(id,checkIn,checkOut):
    bookings = Booking.objects.filter(homeId=id).values()
    booking_list = list(bookings)
    for booking in bookings:
        checkOut = utc.localize(checkOut)
        checkIn = utc.localize(checkIn)
        if ( booking['checkOut'] >= checkIn and booking['checkIn'] <= checkIn ):
            return False
        if ( booking['checkOut'] >= checkOut and booking['checkIn'] <= checkOut ):
            return False
    return True