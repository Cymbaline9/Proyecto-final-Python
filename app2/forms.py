from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class Curso_form(forms.Form):
    nombre =  forms.CharField(max_length=40)
    comision = forms.IntegerField()


class Alumno_form(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    email = forms.EmailField()

class Profesor_form(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    email = forms.EmailField()
    materia = forms.CharField(max_length=40)


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Constraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña" , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email' , 'password1' , 'password2']
        help_text = {k:"" for k in fields}
