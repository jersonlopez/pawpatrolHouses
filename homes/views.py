from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from .models import Homes, Agency, Location

# Create your views here.
def getAllHomes(request):
    agency = Agency.objects.values('name','nit')
    homes = Homes.objects.all().values()
    homes_list = list(homes)
    for home in homes:
        location = Location.objects.filter(id=home['location_id']).values('address','latitude','longitude')
        home['location'] = location[0]
    return JsonResponse({'agency': agency[0], 'homes':homes_list}, safe=False)


def getHomesByCity(request, searchCity):
    agency = Agency.objects.values('name','nit')
    homes = Homes.objects.filter(city=searchCity).values()
    homes_list = list(homes)
    for home in homes:
        location = Location.objects.filter(id=home['location_id']).values('address','latitude','longitude')
        home['location'] = location[0]
    return JsonResponse({'agency': agency[0], 'homes':homes_list}, safe=False)
