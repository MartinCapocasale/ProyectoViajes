from django.shortcuts import render, redirect
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

def crear_hotel(request):
    #Post
    if request.method == "POST":
        formulario = NuevoHotel(request.POST)

        if formulario.is_valid():
            info_hotel = formulario.cleaned_data

            hotel = Hotel(nombre = info_hotel["nombre"],ubicacion = info_hotel["ubicacion"],descripcion = info_hotel["descripcion"],desde = info_hotel["desde"],hasta = info_hotel["hasta"],precio = int(info_hotel["precio"]))
            
            hotel.save()#guardamos en la bdd
            
            return redirect("hoteles")#te redirecciono a la pagina de inicio
        else:
            return render(request,"ProyectoViajesApp/formulario_hotel.html",{"form":formularioVacio})

    #Get y otros
    else:
        formularioVacio = NuevoHotel()
        return render(request,"ProyectoViajesApp/formulario_hotel.html",{"form":formularioVacio})
