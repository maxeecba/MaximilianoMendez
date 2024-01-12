from django.shortcuts import render
from .models import Profesores
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
