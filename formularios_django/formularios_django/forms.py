from django import forms

#### formulario comentform
class ComentForm(forms.Form):
    name = forms.CharField(max_length=100, label='Escribe tu nombre', help_text='100 caracteres maximo') # campo de texto para el nombre del usuario
    url =  forms.URLField(label="Tu sitio web", required=False, initial= "http://") # campo de texto para el URL del autor
    comment = forms.CharField() # campo de texto para el comentario