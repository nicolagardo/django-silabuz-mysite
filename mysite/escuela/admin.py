from django.contrib import admin
from .models import (
    Alumno,
    Profesor,
    Salon
)
# Register your models here.
@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name'

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
