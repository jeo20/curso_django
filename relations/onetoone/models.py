from django.db import models


#Clase Place
class Place(models.Model):
    name = models.CharField(max_length=50) # Nombre del lugar
    address = models.CharField(max_length=50) #  Dirección del lugar
    
    def __str__(self):
        return self.name #  Devuelve el nombre como cadena de texto para mostrar en la interfaz gráfica



#Clase Restaurant
class Restaurant(models.Model):
    place =  models.OneToOneField(Place, on_delete=models.CASCADE, primary_key = True) #Llave foranea a la clase Place
    numbers_of_employees = models.IntegerField(default=1) # Campo de numeros enteros con valor por defecto 1
    
    def __str(self): # Metodo que devuelve el nombre del restaurante como cadena
        return self.place.name #  Devuelve el campo 'name' de la clase Place, es decir, el nombre del lugar donde se encuentra el restaurant