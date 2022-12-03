from django.contrib import admin
<<<<<<< HEAD
from .models import (
    Alumno,
    Profesor,
    Salon
)
# Register your models here.
@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
=======

from .models import Alumno, Directivo, Profesor, Salon, SuperAlumno

# Register your models here.
@admin.register(Alumno)
class AlumnAdmin(admin.ModelAdmin):
>>>>>>> aula07
    list_display = (
        'id',
        'first_name',
        'last_name'
<<<<<<< HEAD

    )

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = (
         'id',
        'first_name',
        'last_name',
        'salario'
    )

@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'idProfesor',
        'aula',
        'hora_entrada',

    )
=======
    )
@admin.register(Profesor)
class ProfeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name'
    )

@admin.register(Directivo)
class DireAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name'
    )

@admin.register(Salon)
class ProfeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'aula'
    )

@admin.register(SuperAlumno)
class SAlumnAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name'
    )
>>>>>>> aula07
