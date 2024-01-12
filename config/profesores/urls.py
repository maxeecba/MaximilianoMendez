from django.urls import path
from .views import padre
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('profesores/',padre)
]
