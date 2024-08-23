from django.http import HttpResponse


def saludo(request):
    return HttpResponse("Hola, JeO")

def despedida(request):
    return HttpResponse("Adiós, JeO")  # <--- Cambio aquí

def adulto(request, edad): # Funcion que evalua si la edad ingresada es mayor de edad o no
    if edad >=  18:
        return HttpResponse("Eres mayor de edad.")
    else:
        return HttpResponse("No eres mayor de edad")