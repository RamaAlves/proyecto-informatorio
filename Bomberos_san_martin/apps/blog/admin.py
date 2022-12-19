from django.contrib import admin
from .models import *

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    ordering = ('id', 'nombre', 'activado', 'fecha_creacion')
    search_fields = ('id', 'nombre', 'activado', 'fecha_creacion')
    list_display = ('id', 'nombre', 'activado', 'fecha_creacion')
    list_filter = ('activado',)

class PostAdmin(admin.ModelAdmin):
    ordering = ('id', 'titulo', 'resumen', 'texto', 'imagen', 'categoria__nombre', 'publicado', 'fecha_creacion', 'usuario')
    search_fields = ('id', 'titulo', 'resumen', 'texto', 'imagen', 'categoria__nombre', 'publicado', 'fecha_creacion')
    list_display = ('titulo', 'resumen', 'imagen', 'categoria', 'publicado', 'fecha_creacion', 'usuario')
    list_filter = ('categoria__nombre', 'publicado')

# habilitar para usar comentarios nativos
# class ComentarioAdmin(admin.ModelAdmin):
#     ordering = ('id', 'id_post', 'autor', 'texto', 'publicado', 'fecha_creacion')
#     search_fields = ('id', 'id_post__titulo', 'autor__username', 'texto', 'publicado', 'fecha_creacion')
#     list_display = ('id', 'id_post', 'autor', 'texto', 'publicado', 'fecha_creacion')
#     list_filter = ('id_post__titulo', 'autor','publicado', 'fecha_creacion')

class EventoAdmin(admin.ModelAdmin):
    ordering = ('id', 'titulo', 'descripcion', 'fecha_creacion', 'usuario__username')
    search_fields = ('id', 'titulo', 'descripcion', 'fecha_creacion')
    list_display = ('titulo', 'descripcion', 'fecha_creacion', 'usuario')
    list_filter = ('id', 'titulo', 'descripcion', 'fecha_creacion', 'usuario__username')

class BomberoAdmin(admin.ModelAdmin):
    ordering = ('id', 'primer_nombre', 'segundo_nombre', 'apellido', 'fecha_nacimiento', 'imagen','biografia','activo','es_jefe','es_directivo')
    search_fields = ('id', 'primer_nombre', 'segundo_nombre', 'apellido', 'fecha_nacimiento', 'activo','es_jefe','es_directivo')
    list_display = ('primer_nombre', 'segundo_nombre', 'apellido', 'fecha_nacimiento', 'imagen','activo','es_jefe','es_directivo')
    list_filter = ('activo','es_jefe','es_directivo')



admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Bombero, BomberoAdmin)
# habilitar para usar comentarios nativos
#admin.site.register(Comentario, ComentarioAdmin)