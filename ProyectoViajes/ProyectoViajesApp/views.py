from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
     return HttpResponse("soy la pagina de inicio")


def base(request):
    return render(request,"ProyectoViajesApp/base.html",{})


def vuelos(request):
    return render(request,"ProyectoViajesApp/vuelos.html",{})

def hoteles(request):
    return render(request,"ProyectoViajesApp/hoteles.html",{})

def excursiones(request):
    return render(request,"ProyectoViajesApp/excursiones.html",{})    