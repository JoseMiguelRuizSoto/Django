from django import forms
from . import models


class NoticiaForm(forms.Form):
    pk = forms.IntegerField()
    titulo = forms.CharField()
    autor = forms.CharField()
    fecha = forms.DateField()
    categoria = forms.CharField()
    imagen = forms.ImageField()
    contenido = forms.CharField()
    