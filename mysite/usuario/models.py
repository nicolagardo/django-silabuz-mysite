from django.db import models

# Create your models here.
class Persona(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dni = models.CharField(max_length=30)
    email = models.EmailField()
    
    class Meta:
        abstract = True



class Alumno(Persona):
    #cursos = models.ForeignKey()  
    promedio_notas = models.FloatField(max_length=4)
    asistencia = models.IntegerField()
    
    class Meta:
        db_table = 'alumnos'

class SuperAlumno(Alumno):

    def saludo():
        return f'hola soy el alumno'

    class Meta:
        proxy = True

class Profesor(Persona):
    sueldo = models.FloatField()
    horario = models.DateTimeField()


class Cargo:
    name_cargo = models.CharField(max_length=30)



# class Directivo(Persona):
#     cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, null= True)
#     escuela = models.ManyToManyField()


# class EscuelaDirectivo:
#     directivo = models.ForeignKey(Directivo)
#     escuela = models.ForeignKey(Escuela)
#     is_active = models.BooleanField()