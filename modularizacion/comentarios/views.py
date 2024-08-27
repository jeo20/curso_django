from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def test(request):
    return HttpResponse("Funciona correctamente aplicacion comentarios")

def create(request):
#    comment = Comment(name="Jorge", score = 5, comment = "Este es un comentario") # Creo manualmente un nuevo objeto de la clase Comment
#    comment.save() # Guardo manualmente el objeto comment en la base de datos
    comment = Comment.objects.create(name = "Eduardo") #  Creo un objeto y  lo guardo en la BD con los valores que le pasamos por parámetros
    return HttpResponse("Ruta para Crear")