from django.shortcuts import render  # importar el modulo de renderizado


def simple(request):
    return render(request, "simple.html")  # Retornar la plantilla simple.html y necesita un diccionario vacio
