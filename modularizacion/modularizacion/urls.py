from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('comentarios/', include("comentarios.urls")) # importa todas las url de comentarios y las agrega a la lista de urls generadas
]
