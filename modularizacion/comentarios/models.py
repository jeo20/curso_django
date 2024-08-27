from django.db import models


# Create your models here.
class Comment (models.Model): #  creamos nuestra clase llamada "Comment", que hereda de "models.Model"
    name = models.CharField(max_length=255, null = False) # Creamos un atributo llamado "name" del tipo CharField
    score = models.IntegerField(default = 3) # Creamos un atributo llamado "score" del tipo IntegerField, y le asigna un valor 3 por defecto
    comment = models.TextField(max_length=1000, null = True) #creamos un atributo llamado "comment" del tipo TextField
    date = models.DateField(null=True) #  Creamos un campo de tipo Date para guardar la fecha del comentario
    signature = models.CharField(max_length = 100, default="Firma") #  Creamos un campo de texto donde mostrará por defecto "firma".
    
    def __str__(self):
        return self.name  #  Creamos un método que retorna el nombre
