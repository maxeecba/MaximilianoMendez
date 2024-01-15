from django.shortcuts import render
from .models import Profesores,Estudiantes
from .forms import ProfesoresForm,EstudiantesForm, EntregablesForm
# Create your views here.
def padre(request):
    return render(request,'profesores/padre.html')

def profesor_formulario(request):
    if request.method == 'POST':
        formulario = ProfesoresForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return render(request, "profesores/formulario_profe.html")
    else: formulario = ProfesoresForm()
    return render(request,'profesores/formulario_profe.html', {'formulario': formulario})

def estudiante_formulario(request):
    if request.method == 'POST':
        formulario = EstudiantesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return render(request, "profesores/formulario_estudiantes.html")
    else: formulario = EstudiantesForm()
    return render(request,'profesores/formulario_estudiantes.html', {'formulario_estudiantes': formulario})

def entregables_formulario(request):
    if request.method == 'POST':
        formulario = EntregablesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return render(request, "profesores/formulario_entregables.html")
    else: formulario = EntregablesForm()
    return render(request,'profesores/formulario_entregables.html', {'formulario_entregables': formulario})

def videos(request):
    return render (request,'profesores/video.html')

#LEER Formulario
def leer_profesores(request):
    profesor = Profesores.objects.all()#todos los profesores de la base de datos
    contexto = {'profesores':profesor} # ace va la lista de profesores
    return render(request,'profesores/leerProfesores.html', contexto)

def eliminar_profesor(request, profesor_nombre):
    profesor = Profesores.objects.filter(nombre=profesor_nombre)
    profesor.delete()
    
    profesores= Profesores.objects.all()
    contexto = {"profesores": profesores}
    return render(request,"profesores/leerProfesores.html",contexto)
    
#LEER Formulario
def leer_estudiantes(request):
    estudiante = Estudiantes.objects.all()#todos los profesores de la base de datos
    contexto = {'estudiantes':estudiante} # ace va la lista de profesores
    return render(request,'profesores/leerEstudiantes.html', contexto)

def eliminar_estudiante(request,estudiante_nombre):
    estudiante= Estudiantes.objects.filter(nombre=estudiante_nombre)
    estudiante.delete()
    
    estudiantes = Estudiantes.objects.all()
    contexto ={'estudiantes':estudiantes}
    return render (request,'profesores/leerEstudiantes.html',contexto)