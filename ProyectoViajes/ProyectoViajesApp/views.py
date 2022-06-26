from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def inicio(request):
     return render(request,"ProyectoViajesApp/index.html",{})


def base(request):
    return render(request,"ProyectoViajesApp/base.html",{})


def vuelos(request):
    vuelos = Vuelo.objects.all()
    return render(request,"ProyectoViajesApp/vuelos.html",{"vuelos":vuelos})

def hoteles(request):
    hoteles = Hotel.objects.all()
    return render(request,"ProyectoViajesApp/hoteles.html",{"hoteles":hoteles})

def excursiones(request):
    excursiones = Excursion.objects.all()
    return render(request,"ProyectoViajesApp/excursiones.html",{"excursiones":excursiones})    