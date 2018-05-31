from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
import json
from .models import Homes, Agency, Location, Booking
from datetime import datetime 
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def getAllHomes(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    fechaLlegada = datetime.strptime(body['checkIn'],'%d-%m-%Y')
    fechaSalida = datetime.strptime(body['checkOut'],'%d-%m-%Y')
    if(fechaLlegada > fechaSalida):
        return JsonResponse({'message':'CheckIn date is lesser than CheckOut date.'}, safe=False)
    if(fechaLlegada==fechaSalida):
        return JsonResponse({'message': 'CheckIn and CheckOut date are equals.'}, safe=False)
    if(body['city']=="CO-MDE"):
        filterCity = 'Medellin'
    elif(body['city']=="CO-BOG"):
        filterCity = 'Bogota'
    elif(body['city']=="CO-CLO"):
        filterCity = 'Cali'
    elif(body['city']=="CO-SMR"):
        filterCity = 'Santa Marta'
    elif(body['city']=="CO-CTG"):
        filterCity = 'Cartagena'
    else:
        return JsonResponse({'message': 'No city selected.'}, safe=False)
    if(body['type']=="1"):
        filterType = "Apartamento"
    elif(body['type']=="2"):
        filterType = "Casa"
    elif(body['type']=="3"):
        filterType = "Luxury"
    else:
        return JsonResponse({'message': 'No type selected.'}, safe=False)
    agency = Agency.objects.values('name','nit')
    homes = Homes.objects.all().filter(city=filterCity, type=filterType).values()
    homes_list = list(homes)
    print('getHomes')
    for home in homes:
        location = Location.objects.filter(id=home['location_id']).values('address','latitude','longitude')
        home['location'] = location[0]
    return JsonResponse({'agency': agency[0], 'homes':homes_list}, safe=False)

@csrf_exempt 
def getHomesByCity(request, searchCity):
    agency = Agency.objects.values('name','nit')
    homes = Homes.objects.filter(city=searchCity).values()
    homes_list = list(homes)
    print('getHomesByCity')
    for home in homes:
        location = Location.objects.filter(id=home['location_id']).values('address','latitude','longitude')
        home['location'] = location[0]
    return JsonResponse({'agency': agency[0], 'homes':homes_list}, safe=False)

@csrf_exempt
def addBooking(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    checkIn = datetime.strptime(body['checkIn'],'%d-%m-%Y')
    checkOut = datetime.strptime(body['checkOut'],'%d-%m-%Y')
    agency = Agency.objects.values('name','nit')
    home = Homes.objects.filter(id=body['id'])[0]
    print(home)
    homeId = home
    booking = Booking.addBooking(checkIn,checkOut,homeId,"sonorks")
    print(booking)
    booking.save()
    return JsonResponse({'agency': agency[0], 'codigo':1, 'mensaje':'Reserva con exito!!!'}, safe=False)


@csrf_exempt
def getBookingsByUser(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    user = body['user']
    agency = Agency.objects.values('name','nit')
    bookings = Booking.objects.filter(userId=user).values()
    booking_list = list(bookings)
    print(booking_list)
    homes = Homes.objects.values()
    homes_list = list(homes)
    
    for home in homes:
        home['booking'] = []
        location = Location.objects.filter(id=home['location_id']).values('address','latitude','longitude')
        home['location'] = location[0]
        for booking in bookings:
            if(booking['homeId_id'] == home['id']):
                home['booking'].append({"checkIn":booking['checkIn'], "checkOut":booking['checkOut'], "bookingId":booking['bookingId']})

    return JsonResponse({'agency': agency[0], 'homes':homes_list}, safe=False)