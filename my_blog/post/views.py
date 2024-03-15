from django.shortcuts import render
from .models import Author, Entry

# Create your views here.
def queries(request):
    # obtener todos los elementos
    authors = Author.objects.all()
    return render(request, 'post/queries.html',{'authors':authors})