from django.db import models


class Publication(models.Model): # Clase publicacion
    title = models.CharField(max_length=30)   # Titulo de la publicación, máx 30 caracteres
    
    def __str__(self): # Devuelve el titulo como string
        return self.title # Devuelve el título de la publicación

class Article(models.Model): #Clase artículo
    headline = models.CharField(max_length=100) #Título principal del articulo, máx 100 carácteres
    publications = models.ManyToManyField(Publication) #Relación muchos a muchos con la clase Publication
    #Permite que un solo articulo pueda estar en varias publicaciones 
    
    def __str__(self): # Devuelve el titulo como string
        return self.headline # Devuelve el título principal del artículo