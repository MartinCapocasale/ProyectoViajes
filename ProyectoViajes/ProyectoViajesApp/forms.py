from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class NuevoHotel(forms.Form):

    nombre = forms.CharField(max_length=30, label = "Nombre:")
    ubicacion = forms.CharField(max_length=60, label= "Ubicacion:")
    descripcion = forms.CharField(max_length=150, label= "Descripcion:")
    desde = forms.DateTimeField(label= "Desde:")
    hasta = forms.DateTimeField(label= "Hasta:")
    precio = forms.DecimalField(label= "Precio:")
    imagen = forms.URLField(label="Imagen URL:")

class NuevoVuelo(forms.Form):

    id_vuelo = forms.IntegerField(label= "Id Vuelo:")
    origen = forms.CharField(max_length=30,label= "Origen:")
    destino = forms.CharField(max_length=30,label= "Destino:")
    ida = forms.DateTimeField(label=  "Ida:")
    vuelta = forms.DateTimeField(label= "Vuelta:")
    precio = forms.DecimalField(label= "Precio:")
    imagen = forms.URLField(label="Imagen URL:")

class NuevoExcursion(forms.Form):

    nombre = forms.CharField(max_length=30,label = "Nombre:")
    ubicacion = forms.CharField(max_length=60,label = "Ubicacion:")
    descripcion = forms.CharField(max_length=150,label = "Descripcion:")
    duracion = forms.IntegerField(label = "Duracion:")
    precio = forms.DecimalField(label = "Precio:")
    imagen = forms.URLField(label="Imagen URL:")

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(label="Email:")
    #passwod1 = forms.CharField(label = "Contraseña:", widget=forms.PasswordInput)
    #passwod2 = forms.CharField(label = "Repetir la Contraseña:", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email']
        help_texts = {k:"" for k in fields}