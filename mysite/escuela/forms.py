from django import forms

class InputForm(forms.Form):

    aula = forms.CharField(max_length=2, label="Nombre Salon")
    hora_entrada = forms.TimeField(
        help_text="Ingrese la hora"
    )