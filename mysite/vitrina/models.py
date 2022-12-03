from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    average_rating = models.FloatField()
    isbn = models.CharField(max_length=10)
    isbn13 = models.CharField(max_length=13)
    language_code = models.CharField(max_length=10)
    num_pages = models.IntegerField()
    ratings_count = models.BigIntegerField()
    text_reviews_count = models.BigIntegerField()
    publication_date = models.DateField(auto_now=True)
    publisher = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "books"
t = """


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
"""