from django.http import HttpResponse
from django.shortcuts import render


def getform(request):
    return render(request, 'form.html', {})

def getgoal(request):
    if request.method != 'GET': # si el metodo no es GET o distinto de GET
        return HttpResponse("El metodo POST no esta soportado para esta ruta")                
    name = request.GET['name']
    return render(request, 'success.html', {'name':name})

def postform(request):
    return render(request, 'postform.html', {})

def postgoal(request):
    if request.method != 'POST':
        return HttpResponse("El metodo POST no esta soportado para esta ruta")
    info = request.POST['info']
    return render(request, 'postsuccess.html', {'info':info})
