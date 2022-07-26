# ProyectoViajes
Proyecto web de viajes con Python y Django

-Version del proyecto = 1.0

-Python Version = 3.10.3

-django.VERSION = 4.0.5

-Bootstrap = 5.1.3 

-Pillow = 9.2.0

El proyecto consiste en una web de viajes, teniendo inicialmente 3 modelos Vuelo, Hotel y Excursion, cada uno con su vista esto sumado a las 
vistas de formulario para la insercion y las de busqueda para podder realizar una busqueda en cada uno de los modelos.
Se agrega una base.html para aplicar herencia a los demas archivos .html, tambien se crea una carpeta raiz de imagenes para obtener imagenes de portadas
de cada template, en cambio para el caso de las cards se utiliza el modelo.URLField para obtener las imagenes adecuada a cada tarjeta.

Se agregan varias cargas a la base de datos con varios ejemplos de vuelos, hoteles y excursiones

Por ultimo se agregan y se prueban el formulario de creacion de objetos y busqueda, y se configura el index.html para mostrar unicamente
los ultimos de cada modelo agregado.

-Para su ejecucion:
Clonar repositorio, inizializar Django, y abrir proyecto completo con IDE.

Ejecutar:
    
    python .\manage.py runserver

ingresar al localhost y el puerto correspondiente para visualizar el proyecto completo.

-Para ingresar al panel de administracion de Django:
    
    ingresar al localhost y el puerto correspondiente/admin

Se crean objetos desde el panel de administracion para probar su funcionalidad y se agrega a cada modelo su nombre correspondiente y un campo de busqueda.

Se agregan vistas de perfiles de usuario, se agrega modulo de login,logout y registro para estos, solo usuarios con privilegios pueden acceder a crear y ver la edicion de su perfil y su avatar

se agregan los mensajes y comentarios en las excursiones
    -se utilizan cvb para la implementacion en la vista de AddCommentView
    -se utiliza mixin para comentar solo estando autenticado