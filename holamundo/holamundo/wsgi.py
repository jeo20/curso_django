"""
El archivo wsgi.py es un componente crucial para ejecutar una aplicación Django con servidores web que implementan 
la interfaz WSGI (Web Server Gateway Interface). WSGI define un estándar para la comunicación entre servidores web y aplicaciones web,
permitiendo la interoperabilidad entre diferentes tecnologías.

Funciones principales:

Punto de entrada para WSGI: Define la interfaz que el servidor web utiliza para comunicarse con la aplicación Django.

Enrutamiento de solicitudes: Mapea las URLs a las vistas correspondientes de la aplicación.

Manejo de diferentes tipos de aplicaciones: Permite ejecutar aplicaciones WSGI y ASGI (Asynchronous Server Gateway Interface)
dentro del mismo proyecto.

Configuración de middleware: Define qué middleware se debe ejecutar para cada solicitud.

"""

"""
WSGI config for holamundo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'holamundo.settings')

application = get_wsgi_application()
