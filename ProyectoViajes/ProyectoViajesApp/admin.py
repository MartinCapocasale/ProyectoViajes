from django.contrib import admin
from .models import *

# Register your models here.

class VueloAdmin(admin.ModelAdmin):
    list_display = ("id_vuelo","origen","destino","precio",)
    search_fields = ("id_vuelo","origen","destino","precio",)

class HotelAdmin(admin.ModelAdmin):
    list_display = ("nombre","ubicacion","precio",)
    search_fields = ("nombre","ubicacion","precio",)

class ExcursionAdmin(admin.ModelAdmin):
    list_display = ("nombre","ubicacion","precio",)
    search_fields = ("nombre","ubicacion","precio",)

admin.site.register(Vuelo,VueloAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Excursion, ExcursionAdmin)

admin.site.register(Avatar)
