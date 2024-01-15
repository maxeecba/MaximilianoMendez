from django.urls import path
from .views import padre,profesor_formulario, estudiante_formulario,entregables_formulario,videos,leer_profesores,eliminar_profesor,leer_estudiantes,eliminar_estudiante,editar_profesor
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('',padre, name= "inicio"),
    path('formulario_profesor/',profesor_formulario, name= "profesores_name"),
    path('formulario_estudiante/',estudiante_formulario, name='est_form'),
    path('formulario_entregables/',entregables_formulario, name='entregables_form'),
    path("videos/",videos,name='videos'),
    path("leerprofesores/",leer_profesores,name='leerprofesores2'),
    path("eliminarprofesor/<profesor_nombre>/",eliminar_profesor,name='eliminarprofesor'),
    path("leerestudiantes/",leer_estudiantes,name='leer_estudiantes'),
    path("eliminarestudiante/<estudiante_nombre>/",eliminar_estudiante,name='eliminarestudiante'),
    path('editarProfesor/<profesor_nombre>/', editar_profesor, name="EditarProfesor")
]
