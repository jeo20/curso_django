from django.db import models

# Create your models here.
class Reporter(models.Model): # clase reporter
    first_name =  models.CharField(max_length=30) #  campo de texto first_name con longitud maxima de  30 caracteres
    last_name =  models.CharField(max_length=30) # campo de texto para el apellido del periodista
    email =  models.EmailField() #  campo de correo electronico
    
    def __str__(self):
        return self.email # retorna el email del periodista
    

class Article(models.Model): # clase article
    headline = models.CharField(max_length=100) #  titulo del articulo
    pub_date = models.DateField() #  fecha de publicacion
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE) # clave foranea a la tabla reptorter
    
    def __str__(self): 
        return self.headline #  devuelve el titulo del articulo