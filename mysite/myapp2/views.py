from django.shortcuts import render, HttpResponse
from django.views import View

from django.views.generic import ListView
from vitrina.models import Books
from .forms import InputForm

from django.views.decorators.cache import cache_page
from .tasks import send_book

# Create your views here.
class IndexView(View):
    template = "prueba56.html"
    contexto = {
        "title": "desarrollador django",
        "numero": 2
    }
    def get(self, request):

        return render(request, self.template, self.contexto) 

class BookList2(ListView):
    model = Books
    template_name = 'book22.html'

def book(request):
    pass

#@cache_page(60*15)
def select_book(request, id):
    template = "oneBook.html"
    book = Books.objects.filter(id= id)
    request.session["authors"] = book[0].authors
    contexto = {
        "book": book[0],
        "form": InputForm()
    }
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            send_book.delay(form.cleaned_data["name"], form.cleaned_data["email"])
            print(form.cleaned_data["name"], form.cleaned_data["email"])
            return HttpResponse(f'{form.cleaned_data["name"]} {form.cleaned_data["email"]}')
    return render(request, template, contexto)

def author(request, id):
    template = "author.html"
    contexto = {}
    contexto["author"] = request.session["authors"]
    return render(request, template, contexto)



t1 = """
Modificar la vista actual y añadir los siguientes atributos.

language_code

publisher

text_reviews_count

Luego con los nuevos atributos, filtrar los registros en base a
 los siguientes datos:

publisher debe tener un tamaño menor igual a 20

text_reviews_count debe ser mayor 10

Luego con la información filtrada, añadir el siguiente tag.

Volver en mayúsculas language_code

Consideraciones
Hacer uso de and al momento de concatenar el if para realizar
 correctamente el filtrado.

 https://github.com/nicolagardo/django-silabuz-mysite

"""













taller = """

Taller caché
Para recordar, ¿qué es el caché?. Es un componente que se encarga de guardar solicitudes q
ue hagamos para que en un futuro estás sean mucho más rápidas.

Por ejemplo, una solicitud que realizamos muchas veces, en temas de costo de las solicitudes
 se harían mucho más caras debido a la gran cantidad.

Su funcionamiento se basa en la siguiente lógica.

Dada una URL, try encontrar la página in cache
if la página is in cache:
    return la página en guardada en cache
else:
    generar la página
    guardar la página generada in cache (for next time)
    return la página generada
Entonces, cada vez que se realiza una query o solicitud a la página,
 esta misma se almacena para ser retornada directamente sin generar la información de 
 nuevo.

Ventajas
Vuelve más rápida solicitudes pesadas.

Genera un dinamismo más fluido al no cargas innecesarias.

Desventajas
Genera muchos peso en la información almacenada.

Se tiene que seleccionar bien que información se va a almacenar.

Django permite hacer el cache de distintas querys, vistas, solicitudes.
 Para poder crear este sistema dentro de nuestra aplicación seguiremos los pasos
  a continuación.

pip install python-memcached

"""

