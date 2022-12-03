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
        db_table = "books2"