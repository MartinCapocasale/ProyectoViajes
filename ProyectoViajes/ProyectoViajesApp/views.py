from telnetlib import LOGOUT
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout, authenticate 
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    vuelos = Vuelo.objects.all().latest('id')
    hoteles = Hotel.objects.all().latest('id')
    excursiones = Excursion.objects.all().latest('id')

    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(usuario=request.user)
            url = avatar.imagen.url
        except:
            url = "/media/avatar/perfil_default.png"   
        return render(request,"ProyectoViajesApp/index.html",{"excursiones":excursiones,"vuelos":vuelos,"hoteles":hoteles,"url":url})
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

def register_request(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect("inicio")
            else:
                return redirect("login")
        return render(request,"ProyectoViajesApp/register.html",{"form":form})
            
    form = UserRegisterForm()
        
    return render(request,"ProyectoViajesApp/register.html",{"form":form})
    
def logout_request(request):
    logout(request)
    return redirect("inicio")
    

@login_required    
def editar_perfil(request):

    user = request.user

    if request.method == "POST":
        form =  UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            user.save()

            return redirect("inicio")
    else:
        form = UserEditForm(initial={"email":user.email,"first_name":user.first_name,"last_name":user.last_name})

    return render(request,"ProyectoViajesApp/editar_perfil.html",{"form":form})

@login_required    
def agregar_avatar(request):
    
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            avatar = Avatar(usuario=user, imagen=form.cleaned_data["imagen"])
            avatar.save()
            return redirect("inicio")
    else:
        form = AvatarForm()
    return render(request,"ProyectoViajesApp/agregar_avatar.html",{"form":form})


def base(request):
    return render(request,"ProyectoViajesApp/base.html",{})

def acerca_de(request):
    acerca = Acerca_de.objects.all()
    return render(request,"ProyectoViajesApp/acerca_de.html",{"acerca":acerca})

def vuelos(request):
    vuelos = Vuelo.objects.all()
    return render(request,"ProyectoViajesApp/vuelos.html",{"vuelos":vuelos})

def hoteles(request):
    hoteles = Hotel.objects.all()
    return render(request,"ProyectoViajesApp/hoteles.html",{"hoteles":hoteles})


def excursiones(request):
    excursiones = Excursion.objects.all()
    return render(request,"ProyectoViajesApp/excursiones.html",{"excursiones":excursiones})

@login_required 
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

@login_required 
def eliminar_hotel(request,hotel_id):

    hotel = Hotel.objects.get(id=hotel_id)
    if request.method == "POST":
        hotel.delete()
        return redirect("hoteles")

    return render(request,"ProyectoViajesApp/eliminar_hotel.html",{"hotel":hotel})

@login_required 
def editar_hotel(request,hotel_id):

    hotel = Hotel.objects.get(id=hotel_id)

    if request.method == "POST":
        
        formulario = NuevoHotel(request.POST)

        if formulario.is_valid():
            
            info_hotel = formulario.cleaned_data
            
            hotel.nombre = info_hotel["nombre"]
            hotel.ubicacion = info_hotel["ubicacion"]
            hotel.descripcion = info_hotel["descripcion"]
            hotel.desde = info_hotel["desde"]
            hotel.hasta = info_hotel["hasta"]
            hotel.precio = info_hotel["precio"]
            hotel.imagen = info_hotel["imagen"]
            hotel.save()

            return redirect("hoteles")

    # get
    formulario = NuevoHotel(initial={"nombre":hotel.nombre, "ubicacion":hotel.ubicacion, "descripcion": hotel.descripcion,"desde":hotel.desde, "hasta":hotel.hasta, "precio": hotel.precio, "imagen": hotel.imagen})
    
    return render(request,"ProyectoViajesApp/editar_hotel.html",{"form":formulario})

@login_required 
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

@login_required 
def eliminar_vuelo(request,vuelo_id):

    vuelo = Vuelo.objects.get(id=vuelo_id)
    if request.method == "POST":
        vuelo.delete()
        return redirect("vuelos")

    return render(request,"ProyectoViajesApp/eliminar_vuelo.html",{"vuelo":vuelo})

@login_required 
def editar_vuelo(request,vuelo_id):

    vuelo = Vuelo.objects.get(id=vuelo_id)

    if request.method == "POST":
        
        formulario = NuevoVuelo(request.POST)

        if formulario.is_valid():
            
            info_vuelo = formulario.cleaned_data
            
            vuelo.id_vuelo = info_vuelo["id_vuelo"]
            vuelo.origen = info_vuelo["origen"]
            vuelo.destino = info_vuelo["destino"]
            vuelo.ida = info_vuelo["ida"]
            vuelo.vuelta = info_vuelo["vuelta"]
            vuelo.precio = info_vuelo["precio"]
            vuelo.imagen = info_vuelo["imagen"]
            vuelo.save()

            return redirect("vuelos")

    # get
    formulario = NuevoVuelo(initial={"id_vuelo":vuelo.id_vuelo, "origen":vuelo.origen, "destino": vuelo.destino,"ida":vuelo.ida, "vuelta":vuelo.vuelta, "precio": vuelo.precio,"imagen": vuelo.imagen})
    
    return render(request,"ProyectoViajesApp/editar_vuelo.html",{"form":formulario})

@login_required 
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
@login_required 
def eliminar_excursion(request,excursion_id):

    excursion = Excursion.objects.get(id=excursion_id)
    if request.method == "POST":
        excursion.delete()
        return redirect("excursiones")

    return render(request,"ProyectoViajesApp/eliminar_excursion.html",{"excursion":excursion})

@login_required 
def editar_excursion(request,excursion_id):

    excursion = Excursion.objects.get(id=excursion_id)

    if request.method == "POST":
        
        formulario = NuevoExcursion(request.POST)

        if formulario.is_valid():
            
            info_excursion = formulario.cleaned_data
            
            excursion.nombre = info_excursion["nombre"]
            excursion.ubicacion = info_excursion["ubicacion"]
            excursion.descripcion = info_excursion["descripcion"]
            excursion.duracion = info_excursion["duracion"]
            excursion.precio = info_excursion["precio"]
            excursion.imagen = info_excursion["imagen"]
            excursion.save()

            return redirect("excursiones")

    # get
    formulario = NuevoExcursion(initial={"nombre":excursion.nombre, "ubicacion":excursion.ubicacion, "descripcion": excursion.descripcion,"duracion":excursion.duracion, "precio":excursion.precio, "imagen": excursion.imagen})
    
    return render(request,"ProyectoViajesApp/editar_excursion.html",{"form":formulario})

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

