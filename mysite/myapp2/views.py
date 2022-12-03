from django.shortcuts import render
from django.views import View

from django.views.generic import ListView
from vitrina.models import Books
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