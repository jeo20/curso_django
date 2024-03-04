from django.shortcuts import render # importar el modulo de renderizado

def simple(request):
    return render(request, "simple.html",  {})  # Mostrar la vista simple.html y enviarle un diccionario vacio para que no haya errores en la  
# la vista es una funcion que recibe una vista sencilla que devuelve un string acompañado del request

def dinamico(request, name):
    categories = ['code','design','marketing','business'] # lista con las categorias posibles para mostrar en la pagina
    context = {'name': name, 'categories': categories} # creamos una variable context y guardamos un diccionario con el nombre como clave(name que recibimos de parametro) y lo pasamos al template
    return render(request, 'dinamico.html', context)  # se le pasa al render el request y el nombre de la plantilla con los 
    # en este caso, se le pasa al parametro 'numero' como nombre de variable y se obtiene su valor desde