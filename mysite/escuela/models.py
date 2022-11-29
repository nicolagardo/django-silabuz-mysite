from django.db import models

# Create your models here.
class Persona(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dni = models.CharField(max_length=10)
    email = models.EmailField()

    def nombre_completo(self):
        return f'{self.first_name} - {self.last_name}'
    class Meta:
        abstract = True


class Alumno(Persona):
    
    promedio_notas = models.FloatField()
    asisitencia = models.IntegerField()

class SuperAlumno(Alumno):

    def saludo(self):
        return f'Hola'

    class Meta:
        proxy = True    

class Profesor(Persona):
    salario = models.FloatField(null= True)
    horas_trabajo = models.IntegerField()

    class Meta:
        db_table = 'profesor'
        verbose_name_plural = 'profesores'



class Cargo1(models.Model):
    name_cargo = models.CharField(max_length=20)

class Directivo(Persona):
    cargo = models.ForeignKey(Cargo1, on_delete= models.CASCADE, null= True)

    class Meta:
        db_table = 'dire'

class Salon(models.Model):
    id_profesor= models.ForeignKey(Profesor, on_delete=models.CASCADE)
    aula = models.CharField(max_length=2)
    hora_entrada = models.TimeField(auto_now=True)

a  = """
Añadir el id del profesor a la tabla salón para relacionar a un profesor con un salón.
"""

#alumno = Alumno()

#alumno.nombre_completo()


b = """

Cree un modelo Evaluacion la cual será una clase padre, esta deberá tener los siguientes atributos. Recuerde que esta debe ser abstract.

Hora y fecha

Curso: máximo 30 caracteres

Evaluador: máximo 50 caracteres

Cree un modelo Examen_Final el cual herede de Evaluacion, y añade los siguiente atributos.

Atributos

Duración del examen: minutos como cantidad entera

Número de preguntas: entero

Puntaje total: entero

Métodos

Puntaje * pregunta: debe retornar la división del número de preguntas entre el puntaje total.
Cree un modelo Proyecto el cual herede de Evaluacion y añada los siguientes campos.

Tema del proyecto: máximo 100 caracteres

Número de grupos

Del modelo Proyecto crea un modelo proxy, el cual ordena los registros por el tema del proyecto.
"""


