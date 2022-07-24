from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar

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

    #foto = forms.ImageField(required=False)
    email = forms.EmailField(label="Email:")
    password1: forms.CharField(label="Contraseña:",widget=forms.PasswordInput)
    password2: forms.CharField(label="Confirmar Contraseña:",widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre:", required=False)
    last_name = forms.CharField(label="Apellido:", required=False)

    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']
       # help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    #foto = forms.ImageField(required=False)
    email = forms.EmailField(label="Email:")
    password1: forms.CharField(label="Contraseña:",widget=forms.PasswordInput)
    password2: forms.CharField(label="Confirmar Contraseña:",widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre:")
    last_name = forms.CharField(label="Apellido:")
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']
        #help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="Imagen")

    class Meta:
        model = Avatar
        fields = ['imagen']
        #help_texts = {k:"" for k in fields}
