"""
El archivo views.py es un componente fundamental en el desarrollo de aplicaciones con Django.
Es donde se definen las vistas, que son las funciones que se encargan de procesar las solicitudes del usuario
y generar las respuestas correspondientes.

Funciones principales:

    Procesar solicitudes HTTP:
    Las vistas reciben las solicitudes HTTP del usuario, como GET, POST, PUT, DELETE, etc.
    Acceder a la base de datos: Las vistas pueden acceder a la base de datos para recuperar, modificar o eliminar datos.

    Generar respuestas:
    Las vistas generan las respuestas que se enviarán al usuario, como páginas web, archivos JSON, XML, etc.
    Utilizar plantillas: Las vistas pueden utilizar plantillas HTML para generar respuestas dinámicas.

    Redireccionar a otras URLs:
    Las vistas pueden redireccionar al usuario a otras URLs de la aplicación
"""
from django.http import HttpResponse #  Clase base para construir respuestas HTTP


def saludo(request): # las funciones siempre reciben el parametro request
    return HttpResponse("Hola Mundo") # Devuelve una respuesta HTTP con el mensaje "Hola Mundo"
    
def despedida(request):
    return HttpResponse("Despedida") # Devuelve una respuesta HTTP con el mensaje "Despedida"

def adulto(request, edad): # Funcion que evalua si la edad ingresada es mayor de edad o no
    if edad >=  18:
        return HttpResponse("Eres mayor de edad.")
    else:
        return HttpResponse("No eres mayor de edad")