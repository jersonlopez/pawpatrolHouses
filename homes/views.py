from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from .models import Homes

# Create your views here.
def getAllHomes(request):

    homes = Homes.objects.all().values()
    homes_list = list(homes)
    return JsonResponse(homes_list, safe=False)
