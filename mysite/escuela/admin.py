from django.contrib import admin

from .models import Alumno, Directivo, Profesor, Salon, SuperAlumno

# Register your models here.
@admin.register(Alumno)
class AlumnAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name'
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