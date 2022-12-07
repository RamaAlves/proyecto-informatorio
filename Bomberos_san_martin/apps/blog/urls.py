from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path('', views.index, name='index'),
    path('contacto', views.contacto, name='contacto'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('aspirantes', views.aspirantes, name='aspirantes'),
    path('donacion', views.donacion, name='donacion'),
    path('perfil', views.perfil, name='perfil'), 
]
