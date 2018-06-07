from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
import json
from .models import Homes, Agency, Location, Booking
from . import verify
from datetime import datetime 
from . import validations
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def getAllHomes(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    fechaLlegada = datetime.strptime(body['checkIn'],'%d-%m-%Y')
    fechaSalida = datetime.strptime(body['checkOut'],'%d-%m-%Y')
    if(validations.dateValidation(fechaLlegada, fechaSalida)==1):
        return JsonResponse({'message':'CheckIn date is later than CheckOut date.'}, safe=False)
    if(validations.dateValidation(fechaLlegada,fechaSalida)==2):
        return JsonResponse({'message': 'CheckIn and CheckOut date are equals.'}, safe=False)
    filterCity=validations.filterCity(body['city'])
    if(filterCity=='void'):
        return JsonResponse({'message': 'No city selected.'}, safe=False)
    if(filterCity=='invalid'):
        return JsonResponse({'message': 'Invalid City type selected.'}, safe=False)         
    filterType=validations.filterType(body['type'])
    if(filterType=='void'):
         return JsonResponse({'message': 'No type selected.'}, safe=False)
    if(filterType=='invalid'):
         return JsonResponse({'message': 'Invalid type selected.'}, safe=False)      
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
    token = request.META['HTTP_TOKEN']
    #print(token)
    token_valid = verify.verificar(token)
    if(token_valid != "Error"):
        print("uid: ",token_valid)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        checkIn = datetime.strptime(body['checkIn'],'%d-%m-%Y')
        checkOut = datetime.strptime(body['checkOut'],'%d-%m-%Y')
        agency = Agency.objects.values('name','nit')
        home = Homes.objects.filter(id=body['id'])[0]
        print(home)
        homeId = home
        booking = Booking.addBooking(checkIn,checkOut,homeId,token_valid)
        print(booking)
        booking.save()
        return JsonResponse({'agency': agency[0], 'codigo':1, 'mensaje':'Reserva con exito!!!'}, safe=False)
    else:
        return JsonResponse({'agency': 12}, safe=False)    


@csrf_exempt
def getBookingsByUser(request):
    token = request.META['HTTP_TOKEN']
    #print(token)
    token_valid = verify.verificar(token)
    if(token_valid != "Error"):
        agency = Agency.objects.values('name','nit')
        bookings = Booking.objects.filter(userId=token_valid).values()
        booking_list = list(bookings)
        #print(booking_list)
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
    else:
        return JsonResponse({'agency': 12}, safe=False) 


@csrf_exempt
def removeBooking(request):
    token = request.META['HTTP_TOKEN']
    #print(token)
    token_valid = verify.verificar(token)
    if(token_valid != "Error"):
        agency = Agency.objects.values('name','nit')
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        bookingId = body['bookingId']
        booking = Booking.objects.filter(bookingId=bookingId).delete()
        return JsonResponse({'agency': agency[0], 'codigo':1, 'mensaje':'Cancelación con exito!!!'}, safe=False)
    else:
        return JsonResponse({'agency': 12}, safe=False)
