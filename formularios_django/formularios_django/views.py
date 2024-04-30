from django.shortcuts import render
from django.http import HttpResponse
from .forms import ComentForm, ContactForm

def form(request):
    coment_form = ComentForm({'name': 'Jorge', 'url': 'http://jeo.com','comment':'comentario jeo'}) # crea el formulario con los datos iniciales
    return render(request, 'form.html',{'coment_form':coment_form})

def goal(request): # funcion que recibe el formulario
    if request.method != 'POST':
        return HttpResponse("Metodo no permitido") # devuelve "metodo no permitido" cuando es distinto de GET
    
    return HttpResponse(request.POST['name']) # devuelve el nombre del campo name del formulario

def widget(request):# vista widget, recibe la request del formulario y la muestra en una pagina html
    form = ContactForm
    return render(request, 'widget.html', {'form': form})