from django.db import models

# Create your models here.

class Profesores(models.Model):
    nombre= models.CharField(max_length=30 )
    apellido= models.CharField(max_length= 50)
    email= models.EmailField()
    profesion= models.CharField(max_length= 20)
    
    def __str__(self) -> str:
        return f"{self.nombre},{self.apellido}"
    

class Estudiantes(models.Model):
    nombre= models.CharField(max_length= 30)
    apellido = models.CharField(max_length=30)
    email= models.EmailField()
    
    def __str__(self) -> str:
        return f"{self.nombre}{self.apellido}"

    
class Entregables(models.Model):
    nombre = models.CharField(max_length= 30)
    fecha_de_entrega= models.DateField()
    entregado = models.BooleanField()
    def __str__(self) -> str:
        return self.nombre
    

    
