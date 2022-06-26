from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

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

def crear_Vuelo(request):
    #Post
    if request.method == "POST":
        formulario = NuevoVuelo(request.POST)

        if formulario.is_valid():
            info_vuelo = formulario.cleaned_data

            vuelo = Vuelo(id_vuelo = info_vuelo["id_vuelo"],origen = info_vuelo["origen"],destino = info_vuelo["destino"],ida = info_vuelo["ida"],vuelta = info_vuelo["vuelta"],precio = int(info_vuelo["precio"]))
            
            vuelo.save()#guardamos en la bdd
            
            return redirect("vuelos")#te redirecciono a la pagina de inicio
        else:
            return render(request,"ProyectoViajesApp/formulario_vuelo.html",{"form":formularioVacio})

    #Get y otros
    else:
        formularioVacio = NuevoVuelo()
        return render(request,"ProyectoViajesApp/formulario_vuelo.html",{"form":formularioVacio})

def crear_excursion(request):
    #Post
    if request.method == "POST":
        formulario = NuevoExcursion(request.POST)

        if formulario.is_valid():
            info_excursion = formulario.cleaned_data

            excursion = Excursion(nombre = info_excursion["nombre"],ubicacion = info_excursion["ubicacion"],descripcion = info_excursion["descripcion"],duracion = info_excursion["duracion"],precio = int(info_excursion["precio"]))
            
            excursion.save()#guardamos en la bdd
            
            return redirect("excursiones")#te redirecciono a la pagina de inicio
        else:
            return render(request,"ProyectoViajesApp/formulario_excursion.html",{"form":formularioVacio})

    #Get y otros
    else:
        formularioVacio = NuevoExcursion()
        return render(request,"ProyectoViajesApp/formulario_excursion.html",{"form":formularioVacio})