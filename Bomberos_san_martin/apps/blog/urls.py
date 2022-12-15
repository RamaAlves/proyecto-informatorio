from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

app_name = "blog"
urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('aspirantes/', views.aspirantes, name='aspirantes'),
    path('donacion/', views.donacion, name='donacion'),
    path('perfil/', views.perfil, name='perfil'), 
    
    path('registro/', views.registrarUsuario, name='registro'),
    path('login/', LoginView.as_view(template_name='perfil/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='perfil/logout.html'), name='logout'),
    
    path('crear_post/', views.crearPost, name='crear_post'),
    path('mostrar_post/<int:pk>', views.mostrarPost, name='mostrar_post'),
    path('administrar_posts/', views.administrarPosts, name='administrar_posts'),
    path('actualizar_post/<int:pk>', views.actualizarPost, name='actualizar_post'),
    path('eliminar_post/<int:pk>', views.eliminarPost, name='eliminar_post'),
    
    path('administrar_categorias/', views.administrarCategorias, name='administrar_categorias'),
    path('agregar_categoria/', views.agregarCategoria, name='agregar_categoria'),
    path('actualizar_categoria/<int:pk>', views.actualizarCategoria, name='actualizar_categoria'),
    path('eliminar_categoria/<int:pk>', views.eliminarCategoria, name='eliminar_categoria'),
    
    path('administrar_eventos/', views.administrarEventos, name='administrar_eventos'),
    path('agregar_evento/', views.agregarEvento, name='agregar_evento'),
    path('actualizar_evento/<int:pk>', views.actualizarEvento, name='actualizar_evento'),
    path('eliminar_evento/<int:pk>', views.eliminarEvento, name='eliminar_evento'),
    
    path('administrar_bomberos/', views.administrarBomberos, name='administrar_bomberos'),
    path('agregar_bombero/', views.agregarBombero, name='agregar_bombero'),
    path('actualizar_bombero/<int:pk>', views.actualizarBombero, name='actualizar_bombero'),
    path('eliminar_bombero/<int:pk>', views.eliminarBombero, name='eliminar_bombero')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
