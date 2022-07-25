from asyncio.windows_events import NULL
from django.test import TestCase

from .models import Excursion, Hotel, Vuelo
# Create your tests here.

class ExcursionTest(TestCase):

    def setUp(self):
        Excursion.objects.create(nombre="Cataratas",ubicacion="Misiones-Argentina",descripcion="Caminar por Pasarelas",duracion="5",precio=10000,imagen="")
        Vuelo.objects.create(id_vuelo=1010,origen="EZE-Buenos Aires", destino="MDP-Mar del Plata",ida="2022-12-10",vuelta="2022-12-17",precio=10000,imagen="")
        Hotel.objects.create(nombre="La Perla",ubicacion="Buenos Aires", descripcion="El mejor hotel de la ciudad",desde="2022-1-1",hasta="2022-12-10",precio=10000,imagen="")

    def test_Excursion_nombre(self):
        excursion = Excursion.objects.get(ubicacion="Misiones-Argentina")
        self.assertEqual(excursion.nombre,"Cataratas")

    def test_Excursion_creada(self):
        excursion = Excursion.objects.get(ubicacion="Misiones-Argentina")
        self.assertNotEquals(excursion,None)

    def test_Vuelo_id(self):
        vuelo = Vuelo.objects.get(ida="2022-12-10")
        self.assertEquals(vuelo.id_vuelo,1010)
    
    def test_Vuelo_creado(self):
        vuelo = Vuelo.objects.get(origen="EZE-Buenos Aires")
        self.assertNotEquals(vuelo,None)
    
    def test_hotel_ubicacion(self):
        hotel = Hotel.objects.get(descripcion="El mejor hotel de la ciudad")
        self.assertEquals(hotel.ubicacion,"Buenos Aires")
    
    def test_hotel_creado(self):
        hotel = Hotel.objects.get(ubicacion="Buenos Aires")
        self.assertNotEquals(hotel,None)

