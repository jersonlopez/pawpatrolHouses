from django.urls import path

from . import views

urlpatterns = [
    path('v1/homes/', views.getAllHomes, name='homes'),
]