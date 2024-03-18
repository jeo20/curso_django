from django.shortcuts import render
from .models import Author, Entry

# Create your views here.
def queries(request):
    # obtener todos los elementos
    authors = Author.objects.all() # SELECT * FROM authors;
    
    # obtener datos filtrados por condicion
    filtered = Author.objects.filter(email= 'lynn58@example.net')  #SELECT * FROM authors WHERE email='lynn58@example.net';
    
    # obtener un objeto unico(filtrado)
    author = Author.objects.get(id = 1)
    
    return render(request, 'post/queries.html',{'authors':authors, 'filtered': filtered, 'author': author}) #  {'authors':authors} -> para pasar variables a la plantilla