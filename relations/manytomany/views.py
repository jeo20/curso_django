from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Publication # importo modelos Article y Publication de la app manytomany

# Create your views here.
def create(request):
    
#### Creo 3 articulos ####    
    art1 = Article(headline="Articulo primero") #  creo un objeto del modelo Article con los datos que le paso en el constructor
    art1.save() #  guarda el primer objeto en BD
    
    art2 = Article(headline="Articulo segundo") # creo un nuevo Artículo con los datos que le paso
    art2.save() # lo guardo en BD (se agrega a Publication.objects.all())
    
    art3 = Article(headline="Articulo tercero") #  creo otro Artículo distinto
    art3.save() #lo agrego a Publication.objects.filter(id=1)
    
#### Creo 7 publicaciones ####
    pub1 = Publication(title="Publicacion primera")
    pub1.save()
    
    pub2 = Publication(title='Publicacion segunda')
    pub2.save()    
    
    pub3 = Publication(title='Publicacion tercera')    
    pub3.save()
    
    pub4 = Publication(title='Publicacion cuarta')    
    pub4.save()
    
    pub5 = Publication(title='Publicacion quinta')        
    pub5.save()
    
    pub6 = Publication(title='Publicacion sexta')        
    pub6.save()
    
    pub7 = Publication(title='Publicacion septima')    
    pub7.save()
    
#### Relaciono  los artículos con las publicaciones ####
    art1.publications.add(pub1) # Agrego la publicación "pub1" al articulo art1
    art1.publications.add(pub2) # Agrego la publicación "pub2" al articulo art1
    art1.publications.add(pub3) # Agrego la publicación "pub3" al articulo art1
    art2.publications.add(pub4) # Agrego la publicación "pub4" al articulo art2
    art2.publications.add(pub5) # Agrego la publicación "pub5" al articulo art2
    art3.publications.add(pub6) # Agrego la publicación "pub6" al articulo art3    
    art3.publications.add(pub7) # Agrego la publicación "pub7" al articulo art3

####  Consultas de ejemplo ####
    result =  art1.publications.all() # Devuelve todas las publicaciones relacionadas con el articulo art1
    return HttpResponse(result)