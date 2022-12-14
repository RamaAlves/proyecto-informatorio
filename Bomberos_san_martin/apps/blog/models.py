from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=False, null=False)
    activado = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categorias'
    
    def __str__(self) :
        return str(self.nombre)
    
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=40, blank=False, null=False)
    resumen = models.CharField(max_length=70, blank=False, null=False)
    texto = models.TextField(max_length=500, blank=False, null=False)
    imagen = models.ImageField(upload_to='post', null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    publicado = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Posteos'

    def __str__(self) :
        return str(self.titulo)

class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE, primary_key=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField(max_length=500, blank=False, null=False)
    publicado = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Comentarios'

    def __str__(self) :
        return str(self.autor+" "+self.texto)

class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=40, blank=False, null=False)
    descripcion = models.TextField(max_length=500, blank=False, null=False)
    fecha_creacion = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Eventos'

    def __str__(self) :
        return str(self.titulo)

class Bombero(models.Model):
    id = models.AutoField(primary_key=True)
    primer_nombre = models.CharField(max_length=20, blank=False, null=False)
    segundo_nombre = models.CharField(max_length=20, blank=True)
    apellido = models.CharField(max_length=20, blank=False, null=False)
    fecha_nacimiento = models.DateField(blank=False, null=False, verbose_name='Fecha de nacimiento')
    imagen = models.ImageField(upload_to='post', null=True)
    biografia = models.TextField(max_length=500, blank=False, null=False)
    activo = models.BooleanField(default=False)
    es_jefe = models.BooleanField(default=False)
    es_directivo = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Bomberos'

    def __str__(self) :
        return str(self.primer_nombre+self.apellido)
    
    def calcular_edad(self):
        return date.today().year - self.fecha_nacimiento.year