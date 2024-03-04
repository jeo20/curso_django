"""
El archivo manage.py es una herramienta fundamental en el desarrollo de aplicaciones con Django. Es un script de Python que se encarga de ejecutar diversos comandos administrativos relacionados con la gestión del proyecto, la base de datos, el servidor y las aplicaciones.

Funciones principales:

Administración del proyecto:
    Creación de nuevas aplicaciones.
    Ejecución de migraciones de la base de datos.
    Creación de superusuarios.
    Impresión de información del proyecto.
    
Gestión de la base de datos:
    Creación, eliminación y sincronización de la base de datos.
    Ejecución de comandos SQL.
    Aplicación de migraciones.
    
Control del servidor:
    Iniciar, detener y reiniciar el servidor de desarrollo.
    Crear un servidor de producción.
    Administración de aplicaciones:
    Creación, eliminación e instalación de aplicaciones.
    Ejecución de comandos específicos de cada aplicación.
"""
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'holamundo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
