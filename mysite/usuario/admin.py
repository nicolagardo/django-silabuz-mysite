from django.contrib import admin
from .models import Alumno

# Register your models here.
@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'promedio_notas'

    )