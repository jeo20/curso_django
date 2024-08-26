from django.shortcuts import render  # importar el modulo de renderizado


def simple(request):
    return render(request, "simple.html", {})  # Retornar la plantilla simple.html, pasamos contexto vacio{}


def dinamico(request, name):
    categories = ['code','design','marketing','business'] 
    # lista con las categorias posibles para mostrar en la pagina
    
    contexto = {'name': name, 'categories': categories} 
    # creamos una variable contexto y guardamos un diccionario con el nombre como clave(name que recibimos de parametro) y el arreglo categories,
    # luego lo pasamos al template
    
    return render(request, 'dinamico.html', contexto)  
    # se le pasa al render el request y el nombre de la plantilla con el contexto
