from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import fields
from django.forms.forms import Form
from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['titulo', 'resumen', 'texto', 'imagen', 'categoria', 'usuario']