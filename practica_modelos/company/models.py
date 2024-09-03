from django.db import models


#### MODELO Salary
class Salary(models.Model):
    amount = models.IntegerField(null=False, blank=False)
    extra_dec = models.BooleanField(default=False)
    extra_jun = models.BooleanField(default=False)
    
    #### RETORNO DE Salary
    def __str__(self):
        return self.amount
    
#### MODELO Job
class Job(models.Model):
    title = models.CharField(max_length=15, blank=False, null=False)
    description = models.TextField(null=True)
    
    #### RELACIONES CON Salary
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
    
    #### RETORNO DE Job
    def __str__(self):
        return self.title


#### MODELO Country
class Country(models.Model):
    name = models.CharField(max_length=15, blank=False, null=False)
    country_code = models.CharField(max_length=6, blank=False, null=False)
    
    #### RETORNO Country
    def __str__(self):
        return self.name 

#### MODELO Location
class Location(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    
    #### RELACION CON Country
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    #### RETORNO DE Location
    def __str__(self):
        return self.name
        
#### MODELO Place
class Place(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    address = models.CharField(max_length=50, blank=False, null=False)
    zip_code = models.CharField(max_length=5, blank=False, null=False)
    
    #### RELACION CON Location
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    #### RETORNO DE Place
    def __str__(self):
        return self.name   
    
#### MODELO Employee
class Employee(models.Model):
    id_number = models.CharField(max_length=10, blank=False, null=False) 
    name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(max_length=30, blank=False, null=False)
    address = models.CharField(max_length=50, blank=False, null=False)
    
    #### RELACIONES CON Job Y Location
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    place = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    #### RETORNO DE Employee
    def __str__(self):
        return self.name
    