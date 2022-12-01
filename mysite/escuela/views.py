from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from datetime import datetime

from dateutil.relativedelta import relativedelta
# Create your views here.
from .forms import InputForm

def index_view(request):
    return HttpResponse("Index")

def index_view2(request):
    if request.method == "GET":
        print("GET")
    elif request.method == "POST":
        print("POST")
        return HttpResponse("Index Post")
    return HttpResponse("Index")

class IndexView(View):
    def get(self, request):
        print("GET de la Clase IndexView")
        return HttpResponse("Respuesta desde la clase")
    
def index_view3(request):
    if request.method == "GET":
        print("GET")
    elif request.method == "POST":
        print("POST")
        return HttpResponse("Index Post")
    return render(request, "index.html")


class IndexView2(View):
    template = "index.html"
    def get(self, request):
        print("GET de la Clase IndexView")
        return render(request, self.template)

class IndexViewWithContex(View):
    hoy = datetime.now()
    fecha_nacimiento = datetime.strptime("15/4/1999", "%d/%m/%Y")
    calculo_edad = relativedelta(hoy, fecha_nacimiento)
    contexto = {
        "name": "Juan",
        "edad": calculo_edad.years
    }       
    template = "index.html"
    def get(self, request):
        print("GET de la Clase IndexView")
        return render(request, self.template, self.contexto)

        
t1 = """

Tarea
Crear dos vistas en forma de función y clase.

Tomar en cuenta que para ambas vistas deben crear un template en el se renderize
 la información.

Vista 1
Contexto: name y edad

Hola, me llamo {{name}} y tengo {{edad}} años.
Tipos de datos
name: string

edad: Date

Consideraciones
En la vista, {{edad}} es un campo que debe ser calculado en base a la fecha de 
nacimiento.

Porque, normalmente en todas las bases únicamente se almacena la fecha de 
nacimiento del usuario y no su edad como tal. Debido a que, este valor depende 
de la fecha de consulta.

Por ejemplo: No es lo mismo ver la edad en el 2020 que en el 2022.
"""
e2 = """
Vista 2
Contexto: name y lista de números de 1 al 4.

La numeración para {{name}} es la siguiente:

- 1
- 2
- 3
- 4
Tipos de datos
name: string

lista de números: array[int]
"""

class IndexViewWithContex2(View):
    
    contexto = {
        "name": "Fulanito",
        "lista": [1,2,3,4]
    }       
    template = "solucion2.html"
    def get(self, request):
        print("GET de la Clase IndexView")
        return render(request, self.template, self.contexto)


def form_index(request):
    contexto = {}
    #contexto['form'] = InputForm()
    if request.method == "GET":
        contexto['form'] = InputForm()
        print("GET")
    elif request.method == "POST":
        print("POST")
        
        template = "form1.html"
        return render(request, template, contexto)
    return render(request, "form1.html", contexto)

    tf = """
    Tarea
Para este taller, crear un formulario en base al modelo Alumno, la ruta para este formulario debe ser /formAlum.

Dentro de los campos se debe tener:

Nombre del alumno

Apellido del alumno

Id del aula a la que pertenece

Luego, cree una ruta dinámica que reciba el nombre del alumno como parámetro. Ejemplo /formAlum/Juan. Además en la ruta dinámica obtenga todos los datos ingresados en el formulario por request.session.

Los datos a recibir dentro de la vista con ruta dinámica son los siguientes:

Apellido del Alumno

Id del aula a la que pertenece

Opcional
Aplicar la misma lógica del item anterior, pero para el modelo profesor.

Ruta formulario: /formProf

Ruta dinámica; /formProf/<first_name>
    
    """
    

