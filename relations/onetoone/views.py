from django.http import HttpResponse
from django.shortcuts import render

from .models import Place, Restaurant


# Create your views here.
def create(request):
    # Crear Place
    place = Place(name="Lugar1", address="Direccion 1") #Se crea el lugar con sus atributos
    place.save() # Se guarda en la base de datos
    
    # Crear Restaurante y relacionarlo con el lugar anterior
    restaurant = Restaurant(place=place, numbers_of_employees=8) # Se crea el restaurante asignandole el lugar definido en place
    restaurant.save() # Se guarda
    
    return HttpResponse(restaurant.place.name) # Retorna el nombre del lugar al que pertenece el restaurante