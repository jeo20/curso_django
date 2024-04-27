from django.db import models

#### MODELO SALARY
class Salary(models.Model):
    #### CAMPOS DE SALARY
    amount = models.IntegerField(null=False, blank=False)
    extra_dec = models.BooleanField(default=False)
    extra_jun = models.BooleanField(default=False)
    
    #### RETORNO DE SALARY
    def __str__(self):
        return self.amount
    
#### MODELO JOB
class Job(models.Model):
    #### DEFINO LOS CAMPOS DE JOB
    title = models.CharField(max_length=15, blank=False, null=False)
    description = models.TextField(null=True)
    
    #### RELACIONES CON SALARY
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
    
    #### RETORNO DE JOB
    def __str__(self):
        return self.title


#### MODELO COUNTRY
class Country(models.Model):
    #### CAMPOS COUNTRY
    name = models.CharField(max_length=15, blank=False, null=False)
    country_code = models.CharField(max_length=6, blank=False, null=False)
    
    #### RETORNO COUNTRY
    def __str__(self):
        return self.name 

#### MODELO LOCATION
class Location(models.Model):
    #### CAMPOS DE LOCATION
    name = models.CharField(max_length=30, blank=False, null=False)
    
    #### RELACION CON COUNTRY
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    #### RETORNO DE LOCATION
    def __str__(self):
        return self.name
        
#### MODELO PLACE
class Place(models.Model):
    #### CAMPOS DE PLACE
    name = models.CharField(max_length=30, blank=False, null=False)
    address = models.CharField(max_length=50, blank=False, null=False)
    zip_code = models.CharField(max_length=5, blank=False, null=False)
    
    #### RELACION CON LOCATION
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    #### RETORNO DE PLACE
    def __str__(self):
        return self.name   
    
#### MODELO EMPLOYEE
class Employee(models.Model):
    #### DEFINO LOS CAMPOS DE EMPLOYEE
    id_number = models.CharField(max_length=10, blank=False, null=False) 
    name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(max_length=30, blank=False, null=False)
    address = models.CharField(max_length=50, blank=False, null=False)
    
    #### RELACIONES CON JOB Y LOCATION
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    place = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    #### RETORNO DE EMPLOYEE
    def __str__(self):
        return self.name
    