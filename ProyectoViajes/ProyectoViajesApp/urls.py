from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio, name="inicio"),
    path('login',login_request, name="login"),
    path('register',register_request, name="register"),
    path('logout',logout_request, name="logout"),
    path('editar_perfil',editar_perfil, name="editar_perfil"),
    path('ver_perfil',ver_perfil, name="ver_perfil"),
    path ('agregar_avatar',agregar_avatar,name="agregar_avatar"),
    #path('base/', base),

    path('acerca_de/',acerca_de,name="acerca_de"),
    path('vuelos/',vuelos,name="vuelos"),
    path('hoteles/',hoteles,name="hoteles"),
    path('excursiones/',excursiones,name="excursiones"),

    path('crear_hotel/',crear_hotel,name="crear_hotel"),
    path('crear_vuelo/',crear_vuelo,name="crear_vuelo"),
    path('crear_excursion/',crear_excursion,name="crear_excursion"),

    path('buscar_ubicacion_hotel/', buscar_ubicacion_hotel, name="buscar_ubicacion_hotel"),
    path('buscar_destino_vuelo/', buscar_destino_vuelo, name="buscar_destino_vuelo"),
    path('buscar_nombre_excursion/', buscar_nombre_excursion, name="buscar_nombre_excursion"),

    path('eliminar_vuelo/<vuelo_id>', eliminar_vuelo, name="eliminar_vuelo"),
    path('eliminar_hotel/<hotel_id>', eliminar_hotel, name="eliminar_hotel"),
    path('eliminar_excursion/<excursion_id>', eliminar_excursion, name="eliminar_excursion"),

    path('editar_vuelo/<vuelo_id>', editar_vuelo, name="editar_vuelo"),
    path('editar_hotel/<hotel_id>', editar_hotel, name="editar_hotel"),
    path('editar_excursion/<excursion_id>', editar_excursion, name="editar_excursion"),

    path('mas_info_vuelo/<vuelo_id>', mas_info_vuelo, name="mas_info_vuelo"),
    path('mas_info_hotel/<hotel_id>', mas_info_hotel, name="mas_info_hotel"),
    path('mas_info_excursion/<excursion_id>', mas_info_excursion, name="mas_info_excursion"),
]
