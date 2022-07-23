from telnetlib import LOGOUT
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout, authenticate 

# Create your views here.
def inicio(request):
    vuelos = Vuelo.objects.all().latest('id')
    hoteles = Hotel.objects.all().latest('id')
    excursiones = Excursion.objects.all().latest('id')

    return render(request,"ProyectoViajesApp/index.html",{"excursiones":excursiones,"vuelos":vuelos,"hoteles":hoteles})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect("inicio")
            else:
                return redirect("login")
        else:
            return redirect("login")
            
    form = AuthenticationForm()
        
    return render(request,"ProyectoViajesApp/login.html",{"form":form})
    
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

            hotel = Hotel(nombre = info_hotel["nombre"],ubicacion = info_hotel["ubicacion"],descripcion = info_hotel["descripcion"],desde = info_hotel["desde"],hasta = info_hotel["hasta"],precio = info_hotel["precio"],imagen = info_hotel["imagen"])
            
            hotel.save()#guardamos en la bdd
            
            return redirect("hoteles")#te redirecciono a la pagina de inicio
        else:
            return render(request,"ProyectoViajesApp/formulario_hotel.html",{"form":formularioVacio})

    #Get y otros
    else:
        formularioVacio = NuevoHotel()
        return render(request,"ProyectoViajesApp/formulario_hotel.html",{"form":formularioVacio})

def crear_vuelo(request):
    #Post
    if request.method == "POST":
        formulario = NuevoVuelo(request.POST)

        if formulario.is_valid():
            info_vuelo = formulario.cleaned_data

            vuelo = Vuelo(id_vuelo = info_vuelo["id_vuelo"],origen = info_vuelo["origen"],destino = info_vuelo["destino"],ida = info_vuelo["ida"],vuelta = info_vuelo["vuelta"],precio = info_vuelo["precio"],imagen = info_vuelo["imagen"])
            
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

            excursion = Excursion(nombre = info_excursion["nombre"],ubicacion = info_excursion["ubicacion"],descripcion = info_excursion["descripcion"],duracion = info_excursion["duracion"],precio = info_excursion["precio"],imagen = info_excursion["imagen"])
            
            excursion.save()#guardamos en la bdd
            
            return redirect("excursiones")#te redirecciono a la pagina de inicio
        else:
            return render(request,"ProyectoViajesApp/formulario_excursion.html",{"form":formularioVacio})

    #Get y otros
    else:
        formularioVacio = NuevoExcursion()
        return render(request,"ProyectoViajesApp/formulario_excursion.html",{"form":formularioVacio})

def buscar_ubicacion_hotel(request):
    if request.method == "POST":
        hotel = request.POST["ubicacion"]
        hoteles = Hotel.objects.filter(ubicacion__icontains=hotel)
        return render(request,"ProyectoViajesApp/buscar_ubicacion_hotel.html",{"hoteles":hoteles})

    else: 
        hoteles = []
        return render(request,"ProyectoViajesApp/buscar_ubicacion_hotel.html",{"hoteles":hoteles})

def buscar_destino_vuelo(request):
    if request.method == "POST":
        vuelo = request.POST["destino"]
        vuelos = Vuelo.objects.filter(destino__icontains=vuelo)
        return render(request,"ProyectoViajesApp/buscar_destino_vuelo.html",{"vuelos":vuelos})

    else: 
        vuelos = []
        return render(request,"ProyectoViajesApp/buscar_destino_vuelo.html",{"vuelos":vuelos})

def buscar_nombre_excursion(request):
    if request.method == "POST":
        excursion = request.POST["nombre"]
        excursiones = Excursion.objects.filter(nombre__icontains=excursion)
        return render(request,"ProyectoViajesApp/buscar_nombre_excursion.html",{"excursiones":excursiones})

    else: 
        excursiones = []
        return render(request,"ProyectoViajesApp/buscar_nombre_excursion.html",{"excursiones":excursiones})