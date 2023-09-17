from django.urls import path
from . import views 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("" , views.inicio , name="home"),
    #path("ver_cursos" , views.ver_cursos),
    #path("alta_curso/<str:nombre>/<int:comision>" , views.alta_curso),
    path("profesores" , views.profesores , name="profesores"),
    path("alumnos" , views.alumnos , name="alumnos"),
    path("alta_curso", views.curso_formulario, name="alta_curso"),
    path("buscar_curso" , views.buscar_curso,name="buscar_curso"),
    path("resultado_curso", views.resultado_curso, name="resultado_curso"),
    path("cursos" , views.cursos, name="cursos"),
    path("mostrar_cursos", views.mostrar_cursos, name="mostrar_cursos"),
    path("info_profesores", views.mostrar_profesores, name="info_profesores"),
    path("alta_profesor", views.alta_profesor, name="alta_profesor"),
    path("buscar_profe" , views.buscar_profe,name="buscar_profe"),
    path("buscar_alumno" , views.buscar_alumno,name="buscar_alumno"),
    path("alta_alumno", views.alta_alumno, name="alta_alumno"),
    path("resultado_alumno", views.resultado_alumno),
    path("resultado_profesor", views.resultado_profesor),
    path("info_alumno", views.mostrar_alumnos, name="info_alumno"),
    path("borrar_curso/<int:id>", views.borrar_curso, name="borrar_curso"),
    path("editar_curso/<int:id>", views.editar_curso, name="editar_curso"),
    path("editar_curso", views.editar_curso, name="editar_curso"),
    path("login", views.login_request, name="login"),
    path("registro", views.registro, name="registro"),
    path("edituser", views.edituser, name="edituser"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("borrar_alumno/<int:id>", views.borrar_alumno, name="borrar_alumno"),
    path("borrar_profesor/<int:id>", views.borrar_profesor, name="borrar_profesor"),
    path("editar_alumno/<int:id>", views.editar_alumno, name="editar_alumno"),
    path("editar_profesor/<int:id>", views.editar_profesor, name="editar_profesor"),

]

