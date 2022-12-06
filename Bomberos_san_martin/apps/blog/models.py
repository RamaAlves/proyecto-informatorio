from django.db import models

# Create your models here.

class Category(models.Model):
    """ modelo de prueba solo para probar migraciones, 
    se puede modificar segun necesidad"""
    title=models.CharField(max_length=255)