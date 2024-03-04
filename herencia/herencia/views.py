from django.shortcuts import render # importar el modulo de renderizado

def index(request):
    return render(request, 'index.html')  # Mostrar la vista "index" en el archivo html correspondiente a esa vista

def herencia(request):
    return render(request, 'herencia.html',{})  # llamada a la plantilla y paso de variables vacia

def ejemplo(request):
    return render(request, 'ejemplo.html', {})

def otra(request):
    return render(request, 'otra.html', {})