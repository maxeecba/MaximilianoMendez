from django.urls import path
from .views import padre,profesor_formulario, estudiante_formulario,entregables_formulario
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('padre/',padre),
    path('formulario_profesor/',profesor_formulario, name= "profesores_name"),
    path('formulario_estudiante/',estudiante_formulario, name='est_form'),
    path('formulario_entregables/',entregables_formulario, name='entregables_form'),
    
]
