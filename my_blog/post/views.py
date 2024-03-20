from django.shortcuts import render
from .models import Author, Entry

# Create your views here.
def queries(request):
    # obtener todos los elementos
    authors = Author.objects.all() # SELECT * FROM authors;
    
    # obtener datos filtrados por condicion
    filtered = Author.objects.filter(email= 'lynn58@example.net')  #SELECT * FROM authors WHERE email='lynn58@example.net';
    
    # obtener un objeto unico(filtrado)
    author = Author.objects.get(id = 1) # SELECT * FROM authors WHERE id=1;
    
    # obtener los 10 primeros elementos
    limits = Author.objects.all()[:10] # SELECT * FROM authors LIMIT 10;
    
    # obtener 5 elementos saltando los primeros 5
    offsets = Author.objects.all()[5:10] # SELECT * FROM authors LIMIT 5 OFFSET 5;
        
    # Retorna render de la request al template  "queries.html" con el contexto definido entre llaves {} de cada metodo
    return render(request, 'post/queries.html',{'authors':authors, 'filtered': filtered, 'author': author, 'limits': limits, 'offsets': offsets})

    