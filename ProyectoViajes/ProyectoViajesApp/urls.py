from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio, name="inicio"),
    #path('base/', base),
    path('vuelos/',vuelos,name="vuelos"),
    path('hoteles/',hoteles,name="hoteles"),
    path('excursiones/',excursiones,name="excursiones"),
    path('crear_hotel/',crear_hotel,name="crear_hotel"),
    path('crear_vuelo/',crear_vuelo,name="crear_vuelo"),
    path('crear_excursion/',crear_excursion,name="crear_excursion"),

]
