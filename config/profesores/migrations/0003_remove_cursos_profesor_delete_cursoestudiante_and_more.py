# Generated by Django 5.0.1 on 2024-01-13 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0002_rename_curso_cursos_nombre_cursos_profesor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursos',
            name='profesor',
        ),
        migrations.DeleteModel(
            name='CursoEstudiante',
        ),
        migrations.DeleteModel(
            name='Cursos',
        ),
    ]