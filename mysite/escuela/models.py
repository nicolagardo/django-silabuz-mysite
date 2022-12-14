from django.db import models

# Create your models here.
class Persona(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dni = models.CharField(max_length=30)
    email = models.EmailField()

    def nombre_completo(self):
        return f'{self.first_name}, - {self.last_name}'
    
    class Meta:
        abstract = True

class Alumno(Persona):
    #cursos = models.ForeignKey()  
    promedio_notas = models.FloatField(max_length=4)
    asistencia = models.IntegerField()
    
    # class Meta:
    #     db_table = 'alumnos'


# alumno = Alumno('pepe', 'Pompin', '2323','pepe@email.com', 10, 10)
# alumno.nombre_completo(9)





# class Profesor(Persona):
#     pass    
#     #first_name = models.CharField(max_length=40)
    #last_name = models.CharField(max_length=40)

    # class Meta:
    #     abstract = True

class Profesor(Persona):
    salario = models.FloatField()
    asistencia = models.DateTimeField()
    registro_notas = models.IntegerField()

    class Meta:
        verbose_name_plural = 'profesores'


a= """
Añadir el id del profesor a la tabla salón para relacionar a un profesor con un salón.
"""

class Salon(models.Model):
    idProfesor = models.ForeignKey(
        Profesor,
        on_delete = models.CASCADE,
        null=True)
    aula = models.CharField(max_length=2)
    hora_entrada = models.TimeField()

    class Meta:
        verbose_name_plural = 'salones'


b = """
Creando nuevos modelos
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