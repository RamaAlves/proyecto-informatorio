from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path('', views.index, name='index'),
    path('contacto', views.contacto, name='contacto'),
    path('aspirantes', views.aspirantes, name='aspirantes'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('perfil', views.perfil, name='perfil'), 
]
