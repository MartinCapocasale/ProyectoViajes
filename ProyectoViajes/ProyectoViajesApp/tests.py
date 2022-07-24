from django.test import TestCase
from .models import Excursion
# Create your tests here.

class ExcursionTest(TestCase):

    def setUp(self):
        Excursion.objects.create(nombre="Cataratas",ubicacion="Misiones-Argentina",descripcion="Caminar por Pasarelas",duracion="5",precio=10000,imagen="")

    def test_Excursion_nombre(self):
        excursion = Excursion.objects.get(ubicacion="Misiones-Argentina")
        self.assertEqual(excursion.nombre,"Cataratas")

    def test_Excursion_creada(self):
        excursion = Excursion.objects.get(ubicacion="Misiones-Argentina")
        self.assertNotEquals(excursion,None)