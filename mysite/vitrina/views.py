from django.shortcuts import render
from django.views.generic import ListView
from .models import Books

class BookList(ListView):
    model = Books
    template_name = 'book.html'