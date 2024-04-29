from django.shortcuts import render
from django.http import HttpResponse
from .forms import ComentForm

def form(request):
    coment_form = ComentForm()
    return render(request, 'form.html',{'coment_form':coment_form})

def goal(request):
    if request.method != 'GET':
        return HttpResponse("Metodo no permitido")
    
    return HttpResponse("Recibido")