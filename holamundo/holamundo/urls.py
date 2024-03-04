"""
El archivo urls.py juega un papel crucial en la configuración de una aplicación Django al definir 
el enrutamiento de las URLs a las vistas correspondientes. 
Es la piedra angular que permite que la aplicación responda a las solicitudes del usuario de manera organizada y eficiente.

Funciones principales:

Enrutamiento de URLs: Define una lista de patrones de URL que se mapean a las vistas de la aplicación.
Importación de vistas: Permite importar las vistas desde diferentes módulos de la aplicación.
Manejo de diferentes tipos de solicitudes: Permite definir diferentes patrones para solicitudes GET, POST, PUT, DELETE, etc.
Configuración de nombres de URL: Asigna nombres únicos a las URLs para facilitar su uso en otras partes de la aplicación.
Inclusión de otras configuraciones de URL: Permite dividir la configuración de URL en diferentes archivos para mayor organización.
"""

"""
URL configuration for holamundo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # Incorpora el panel de administración de Django
from django.urls import path # Utilizado para crear rutas y agregarlas a "urlpatterns"
from . import  views # Importamos las vistas de nuestra app (holamundo)

# Definimos la relacion de cada ruta con su respectiva vista
urlpatterns = [
    path('admin/', admin.site.urls), # Agrega el panel de administración de Django a nuestra app.
    path('saludo/', views.saludo, name= 'saludo'), # La vista saludo está en views.py
    path('despedida/', views.despedida, name='despedida'), # La vista despedida también está en views.py
    path('adulto/<int:edad>/', views.adulto, name='adulto') # La vista adulto recibe un parámetro edad, lo capturamos entre corchetes angulares <>.
]
