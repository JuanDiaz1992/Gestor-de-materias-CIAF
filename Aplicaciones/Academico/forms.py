from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from usuario.models import Estudiante
from django.forms import ModelForm
from .models import Curso
from .choices import materias





class UserRegisterForm (UserCreationForm):
    nombre1 =           forms.CharField(label='Primer Nombre',required=False,)
    email = forms.EmailField()
    password1: forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2: forms.CharField(label='Confirma contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
    
    class form2(forms.ModelForm):
        model = Estudiante
        fields = ['nombre1']



class formFotoPerfil(forms.ModelForm):    
    foto =   forms.ImageField(label='+ Subir foto',required=True, widget=forms.FileInput)
    class Meta:
        model = Estudiante
        fields = ['foto']

class editarDatos(forms.ModelForm):
    nombre1 =           forms.CharField(label='Primer Nombre',required=False,)
    nombre2 =           forms.CharField(label='Segundo Nombre',required=False,)
    primerApellido =    forms.CharField(label='Primer Apellido',required=False,)
    segundoApellido =   forms.CharField(label='Segundo Apellido',required=False,)
    class Meta:
        model = Estudiante
        fields = ['nombre1','nombre2','primerApellido','segundoApellido']


class agregarMateria(forms.ModelForm):
    #nombre = forms.ChoiceField(label='Materias',required=True, widget=forms.ChoiceField)
    nombre = forms.ChoiceField(label='Materias',choices= materias,required=True)
    creditos = forms.DecimalField(label='Creditos',required=True,max_value=5,min_value=1)
    class Meta:
        model = Curso
        fields = ['nombre','creditos']