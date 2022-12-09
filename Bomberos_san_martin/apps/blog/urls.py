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
    path('crear_post/', views.crearPost, name='crear_post'),
    path('login/', LoginView.as_view(template_name='perfil/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='perfil/logout.html'), name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
