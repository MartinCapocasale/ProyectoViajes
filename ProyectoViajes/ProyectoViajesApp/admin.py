from django.contrib import admin
from .models import *

# Register your models here.

class VueloAdmin(admin.ModelAdmin):
    list_display = ("id_vuelo",)
    search_fields = ("id_vuelo","origen",)

class HotelAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)

class ExcursionAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)

admin.site.register(Vuelo,VueloAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Excursion, ExcursionAdmin)
