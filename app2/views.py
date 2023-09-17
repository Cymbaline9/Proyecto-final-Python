from django.shortcuts import render
from app2.models import Curso, Alumno, Profesor, Avatar
from django.template import loader
from django.http import HttpResponse
from app2.forms import Curso_form, Alumno_form, Profesor_form, UserEditForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

def inicio(request):
    return render( request , "index.html")

def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos":cursos}
    plantillas = loader.get_template("plantillas.html")
    documento = plantillas.render(dicc)
    return HttpResponse(documento)


"""
def alta_curso(request, nombre , comision):
    curso = Curso(nombre=nombre , comision=comision)
    curso.save()
    texto = f"Se guardo en el BD el Curso: {curso.nombre} Comision:{curso.comision}"
    return HttpResponse(texto)
"""


@login_required
def profesores(request):
    return render( request , "profesores.html")

def info_profesores(request):
    return render( request , "info_profesores.html")


def alta_profesor(request):
    if request.method == "POST":
        alta_profesor = Profesor_form( request.POST )
        if alta_profesor.is_valid():
            datos = alta_profesor.cleaned_data
            prof = Profesor( nombre=datos['nombre'] , apellido=datos['apellido'], dni=datos['dni'], email=datos['email'])
            prof.save()
          
            return render( request , "alta_profesores.html")
    return render( request , "alta_profesores.html")

@login_required
def alumnos(request):
    return render( request , "alumnos.html")


def alta_alumno(request):
    if request.method == "POST":
        alta_alumno = Alumno_form( request.POST )
        if alta_alumno.is_valid():
            datos = alta_alumno.cleaned_data
            prof = Alumno( nombre=datos['nombre'] , apellido=datos['apellido'], dni=datos['dni'], email=datos['email'])
            prof.save()
          
            return render( request , "alta_alumno.html")
    return render( request , "alta_alumno.html")

def info_alumno(request):
    return render( request , "info_alumno.html")

def curso_formulario(request):

    if request.method == "POST":
        mi_formulario = Curso_form( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos['nombre'] , comision=datos['comision'])
            curso.save()
            return render( request , "formulario.html")
    
    
    return render( request , "formulario.html")




def buscar_curso(request):
    return render( request , "buscar_curso.html")


def buscar_profe(request):
    return render( request , "buscar_profe.html")


def buscar_alumno(request):
    return render( request , "buscar_alumno.html")


def resultado_curso(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render( request, "resultado_busqueda.html", {"cursos": cursos})
    else:
        return HttpResponse("Campo vacio")
    
def resultado_alumno(request):
    if request.GET['dni']:
        dni = request.GET['dni']
        alumno = Alumno.objects.filter(dni__icontains = dni)
        return render( request, "resultado_alumno.html", {"alumnos": alumno})
    else:
        return HttpResponse("Campo vacio")    

    
def resultado_profesor(request):

    if request.GET['dni']:
        dni = request.GET['dni']
        profesor = Profesor.objects.filter(dni__icontains = dni)
        return render( request, "resultado_profesores.html", {"profesores": profesor})
    else:
        return HttpResponse("Campo vacio")
    

    
def cursos(request):
    return render( request , "cursos.html")


def mostrar_cursos(request):
    cursos = Curso.objects.all()
    return render (request, "mostrar_cursos.html", {"cursos":cursos})

def borrar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    cursos = Curso.objects.all()
    return render (request, "mostrar_cursos.html", {"cursos":cursos})

def editar_curso(request, id):
    curso = Curso.objects.get(id=id)

    if request.method == "POST":
        form = Curso_form(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            curso.nombre = datos['nombre']
            curso.comision = datos['comision']
            curso.save()

            cursos = Curso.objects.all()
            return render(request, "mostrar_cursos.html", {"cursos":cursos})
    else:
#acá sería para que me muestre los datos que quiero editar por eso el initial
# cuando va a la página de editar hay un form que cuando envía la data la hace por post y va al if de arriba
         form = Curso_form(initial = {"nombre":curso.nombre, "comision":curso.comision})

    return render (request, "editar_curso.html", {"form":form, "curso":curso})   

@login_required
def mostrar_alumnos(request):
    alumnos = Alumno.objects.all()  
    return render( request, "info_alumno.html", {"alumnos":alumnos})

@login_required
def mostrar_profesores(request):
    profesores = Profesor.objects.all()  
    return render( request, "info_profesores.html", {"profesores":profesores})

def login_request(request):
    if request.method =="POST":
        form = AuthenticationForm (request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            clave = form.cleaned_data.get("password")

            user = authenticate (username = usuario, password = clave)

            if user.is_superuser:
                login (request, user)
                avatar = Avatar.objects.filter(user=request.user.id)
                return render (request, "inicio.html", {"url":avatar[0].image.url})
            else:
                login (request, user)
                return render (request, "inicio.html")

        else:
            return HttpResponse (f"Form incorrecto")    


    form = AuthenticationForm()
    return render(request, "login.html", {"form":form})

def registro(request):
    if request.method =="POST":
        form = UserCreationForm (request.POST)
        if form.is_valid():
            form.save()
#            return render(request , "login.html")
    else:
        form = UserCreationForm()
    return render(request , "registro.html" , {"form":form})

    
    

def edituser (request):
    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info['email']
            password = info['password1']
            usuario.set_password(password)
            usuario.save()
            return render(request, "inicio.html")
    
    else:
        form = UserEditForm(initial={'email':usuario.email})

    return render(request, "edituser.html", {"form":form, "usuario":usuario})

def borrar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)  
    if request.method == "POST":
           alumno.delete()
                       
           alumnos = Alumno.objects.all()
           return render(request, "info_alumno.html", {"alumnos":alumnos})
          
    return render(request, "borrar_alumno.html", {"alumno":alumno})

def borrar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)  
    if request.method == "POST":
           profesor.delete()
                       
           profesores = Profesor.objects.all()  
           return render( request, "info_profesores.html", {"profesores":profesores})
          
    return render(request, "borrar_profesor.html", {"profesor":profesor})

def editar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)

    if request.method == "POST":
        form = Alumno_form(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            alumno.nombre = datos['nombre']
            alumno.apellido = datos['apellido']
            alumno.dni = datos['dni']
            alumno.email = datos['email']
            alumno.save()

            alumnos = Alumno.objects.all()
            return render(request, "info_alumno.html", {"alumnos":alumnos})
    else:

         form = Alumno_form(initial = {"nombre":alumno.nombre, "apellido":alumno.apellido, "dni":alumno.dni, "email":alumno.email})

    return render (request, "editar_alumno.html", {"form":form, "alumno":alumno})  

def editar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)

    if request.method == "POST":
        form = Profesor_form(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            profesor.nombre = datos['nombre']
            profesor.apellido = datos['apellido']
            profesor.dni = datos['dni']
            profesor.email = datos['email']
            profesor.materia = datos['materia']
            profesor.save()

            profesores = Profesor.objects.all()
            return render(request, "info_profesores.html", {"profesores":profesores})
    else:

         form = Profesor_form(initial = {"nombre":profesor.nombre, "apellido":profesor.apellido, "dni":profesor.dni, "email":profesor.email, "materia":profesor.materia})

    return render (request, "editar_profesor.html", {"form":form, "profesor":profesor}) 