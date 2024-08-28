from django.http import HttpResponse
from django.shortcuts import render

from .models import Author, Entry


# Create your views here.
def update(request):
    author = Author.objects.get(id = 1) # SELECT * FROM authors WHERE id=1;
    author.name = "Jorge" # UPDATE authors SET name='Jorge Orellana' WHERE id=1;
    author.email = "jeo20@hotmail.com" # UPDATE  authors SET email='email@email.com.ar' WHERE id=1;
    author.save() #  UPDATE authors SET name='Jorge Orellana', email='email@email.com.ar' WHERE id=1;
    return HttpResponse("Modificado") #  Retorna una respuesta HTTP con un mensaje de texto

def queries(request):
    # obtener todos los elementos
    authors = Author.objects.all() # SELECT * FROM authors;
    
    # obtener datos filtrados por condicion
    #filtered = Author.objects.filter(email= 'lynn58@example.net')  #SELECT * FROM authors WHERE email='lynn58@example.net';
    
    # obtener un objeto unico(filtrado)
    author = Author.objects.get(id = 1) # SELECT * FROM authors WHERE id=1;
    
    # obtener los 10 primeros elementos
    limits = Author.objects.all()[:10] # SELECT * FROM authors LIMIT 10;
    
    # obtener 5 elementos saltando los primeros 5
    offsets = Author.objects.all()[5:10] # SELECT * FROM authors LIMIT 5 OFFSET 5;
    
    # obtener todos los elementos ordenados
    orders = Author.objects.all().order_by(('email')) # SELECT * FROM authors ORDER BY  email;

    # obtener datos filtrados por condicion
    filtered = Author.objects.filter(id__lte=15) #SELECT * FROM authors WHERE id<=15;
    
    # obtener todos los autores que contienen en su nombre la palabra yes
    contains = Author.objects.filter(name__contains="yes") #SELECT * FROM Author WHERE name LIKE '%yes%';
    
    # Retorna render de la request al template  "queries.html" con el contexto definido entre llaves {} de cada metodo
    return render(request, 'post/queries.html',{'authors':authors, 'filtered': filtered, 'author': author, 'limits': limits, 'offsets': offsets, 'orders': orders, 'contains': contains})