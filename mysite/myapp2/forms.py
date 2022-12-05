from django import forms

class InputForm(forms.Form):
    name = forms.CharField(max_length=3)
    email = forms.EmailField()

    t = """
    Crear el envío del libro con django.core.mail (Investigar)
    """