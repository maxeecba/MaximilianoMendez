from django.shortcuts import render
from . import models
# Create your views here.
def padre(request):
    return render(request,'padre.html')