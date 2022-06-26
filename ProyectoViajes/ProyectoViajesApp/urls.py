from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio, name="inicio"),
    #path('base/', base),
    path('vuelos/',vuelos,name="vuelos"),
    path('hoteles/',hoteles,name="hoteles"),
    path('excursiones/',excursiones,name="excursiones")

]
