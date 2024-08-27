from django.http import HttpResponse
from django.shortcuts import render

from .models import Comment


# Create your views here.
def test(request):
    return HttpResponse("Funciona correctamente aplicacion comentarios")

def create(request):
    #comment = Comment(name="Jorge", score = 5, comment = "Este es un comentario") # Creo manualmente un nuevo objeto de la clase Comment
    #comment.save() # Guardo manualmente el objeto comment en la base de datos
    comment = Comment.objects.create(name = "Eduardo") #  Creo un objeto y  lo guardo en la BD con los valores que le pasamos por parámetros
    return HttpResponse("Ruta para Crear Modelos")

def delete(request):
    #comment =  Comment.objects.get(id=1)  # Busco manualmente al comentario con id  1, si no existe lanza una excepción
    #comment.delete() # Elimino manualmente el comentario id = 1, obtenido en el paso anterior
    comment = Comment.objects.filter(id=2).delete()  # Filtro los comentarios por su ID y elimino todos que coincidan
    return HttpResponse("Ruta para Borrar Modelos")