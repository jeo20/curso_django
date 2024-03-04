"""
El archivo asgi.py es un punto de entrada crucial para que los servidores web compatibles con ASGI (Asynchronous Server Gateway Interface) 
puedan servir una aplicación Django. ASGI es un estándar que define cómo los servidores web y las aplicaciones web interactúan
de forma asíncrona, lo que permite un mejor rendimiento y escalabilidad.

Funciones principales:

Punto de entrada para ASGI: Define la interfaz que el servidor web utiliza para comunicarse con la aplicación Django.
Enrutamiento de solicitudes: Mapea las URLs a las vistas correspondientes de la aplicación.
Manejo de diferentes tipos de aplicaciones: Permite ejecutar aplicaciones ASGI y WSGI (Web Server Gateway Interface) dentro del mismo proyecto.
Configuración de middleware: Define qué middleware se debe ejecutar para cada solicitud.

"""
"""
ASGI config for holamundo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'holamundo.settings')

application = get_asgi_application()
