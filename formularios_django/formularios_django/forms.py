from django import forms

#### formulario comentform
class ComentForm(forms.Form):
    name = forms.CharField(max_length=100, label='Escribe tu nombre', help_text='100 caracteres maximo') # campo de texto para el nombre del usuario
    url =  forms.URLField(label="Tu sitio web", required=False, initial= "http://") # campo de texto para el URL del autor
    comment = forms.CharField() # campo de texto para el comentario
    
class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label='Nombre:', widget= forms.TextInput(attrs={'class':'form-control'}))  # nombre del contacto
    email = forms.EmailField(max_length=50, label="Email", widget= forms.EmailInput(attrs={'class':'form-control'}))   # dirección de correo electrónico
    message =  forms.CharField(label="Mensaje", widget= forms.Textarea(attrs={'class':'form-control'}))
    
    def clean_name(self): # funcion para realizar una validacion del nombre especifica
        name = self.cleaned_data.get('name') # obtenemos el valor del campo name
        if name != "Open": # si el nombre es distinto de Open
            raise forms.ValidationError("El nombre es distinto de Open") # lanzamos un error
        else:
            return name # retornamos el valor del campo name