from datetime import date

from django.http import HttpResponse
from django.shortcuts import render

from .models import Article, Reporter


# Create your views here.
def create(request):
    rep = Reporter(first_name="Jorge", last_name="Orellana", email="jorge@gmail.com")
    rep.save()
    
    # articulo 1
    art1 =Article(headline="Noticias 1", pub_date= date(2021,4,17), reporter=rep)
    art1.save()
    
    # articulo 2
    art2 =Article(headline="Noticias 2", pub_date= date(2022,4,17), reporter=rep)
    art2.save()
    
    # articulo 3
    art3 =Article(headline="Noticias 3", pub_date= date(2024,8,28), reporter=rep)  
    art3.save()    
    
    #result = art1.reporter.first_name +" "+ art1.reporter.last_name # devuelve  el nombre del periodista que creo el primer articulo
    #result = rep.article_set.all( ) # devuelve todos los articulos del periodista Jorge Orellana
    result = rep.article_set.filter(headline="Noticias 3") # Devuelve solo el articulo con la headline "Noticias 3"
    return HttpResponse(result)