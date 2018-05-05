from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from .models import Homes, Agency

# Create your views here.
def getAllHomes(request):
    agency = Agency.objects.values('name','nit')
    homes = Homes.objects.all().values()
    homes_list = list(homes)
    return JsonResponse({'agency': agency[0], 'homes':homes_list}, safe=False)


def getHomesByCity(request, searchCity):
    homes = Homes.objects.filter(city=searchCity).values()
    homes_list = list(homes)
    return JsonResponse(homes_list, safe=False)
