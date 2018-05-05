from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
import json
from .models import Homes, Agency, Location
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
        filterCity = ''
    agency = Agency.objects.values('name','nit')
    if(filterCity != ''):
        homes = Homes.objects.all().filter(city=filterCity).values()
    else:
        homes = Homes.objects.all().values()
    homes_list = list(homes)
    for home in homes:
        location = Location.objects.filter(id=home['location_id']).values('address','latitude','longitude')
        home['location'] = location[0]
    return JsonResponse({'agency': agency[0], 'homes':homes_list}, safe=False)

@csrf_exempt 
def getHomesByCity(request, searchCity):
    agency = Agency.objects.values('name','nit')
    homes = Homes.objects.filter(city=searchCity).values()
    homes_list = list(homes)
    for home in homes:
        location = Location.objects.filter(id=home['location_id']).values('address','latitude','longitude')
        home['location'] = location[0]
    return JsonResponse({'agency': agency[0], 'homes':homes_list}, safe=False)
