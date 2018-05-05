from django.urls import path

from . import views

urlpatterns = [
    path('v1/homes/', views.getAllHomes, name='homes'),
    path('v1/homes/<searchCity>', views.getHomesByCity, name='homes'),
]