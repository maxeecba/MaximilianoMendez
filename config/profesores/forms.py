from django import forms
from .models import Profesores,Estudiantes,Entregables

class ProfesoresForm(forms.ModelForm):
    class Meta:
        model = Profesores
        fields = "__all__"
        
class EstudiantesForm(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = "__all__"
        
class EntregablesForm(forms.ModelForm):
    class Meta:
        model = Entregables
        fields = "__all__"