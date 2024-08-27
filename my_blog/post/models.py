from datetime import date

from django.db import models


# Modelo Author Crea una tabla post_author
class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    
    def __str__(self): # Devuelve el nombre del autor como string para mostrar en la interfaz de usuario
        return self.name
    
# Modelo Entry Crea una tabla una tabla post_entry
class Entry(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE) # Defino la clave foranea de la clase Author, va a asignar el id del autor que escriba la entrada 
    # on_delete = models.CASCADE es para que cuando se borre un autor, todos sus entries tambien lo hagan
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    public_date = models.DateField(default=date.today) # fecha de publicacion por defecto hoy
    rating = models.IntegerField(default = 5)
    
    def __str__(self): #  devuelve el titulo del articulo como string para mostrar en la interfaz
        return self.headline