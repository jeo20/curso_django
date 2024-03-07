"""
Creando una clase Django convierte la clase en una tabla en la base de datos 
y cada atributo de la clase se convierte en un campo(columna) de esa tabla
"""
from django.db import models # importamos el modulo que nos permite trabajar con las bases de datos

# Create your models here.
class comments (models.Model): #  creamos nuestra clase llamada "comments", que hereda de "models.Model"
    name = models.CharField(max_length=255, null = False) # Creamos un atributo llamado "name" del tipo CharField
    score = models.IntegerField(default = 3) # Creamos un atributo llamado "score" del tipo IntegerField, y le asigna un valor 3 por defecto
    comment = models.TextField(max_length=1000, null = True) #creamos un atributo llamado "comment" del tipo TextField
    def __str__(self): # el metodo  __str__() convierte un objeto en una cadena de texto
        return self.name  # retorna el nombre del usuario