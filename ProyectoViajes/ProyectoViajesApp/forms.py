from django import forms

class NuevoHotel(forms.Form):

    nombre = forms.CharField(max_length=30, label = "Hotel:")
    ubicacion = forms.CharField(max_length=60, label= "Ubicacion:")
    descripcion = forms.CharField(max_length=150, label= "Descripcion:")
    desde = forms.DateTimeField(label= "Desde:")
    hasta = forms.DateTimeField(label= "Hasta:")
    precio = forms.IntegerField(label= "Precio:")