from django.shortcuts import render, redirect

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseNotFound
from django.db.models import Q
from django.contrib import messages

from .models import Post, Categoria
from .forms import PostForm, RegistrarForm

# Create your views here.
def index(request):
    cat= Categoria.objects.all()

    ordenar = request.GET.get('ordenar')
    print(ordenar)
    if ordenar == 'mas antiguos primero':
        ordenar = 'fecha_creacion'
    else:
        ordenar = '-fecha_creacion'
    
    fecha = request.GET.get('fecha')
    categoria = request.GET.get('categoria')
    busqueda = request.GET.get('buscar')
    if busqueda:
        posts = Post.objects.filter(
            Q(titulo__icontains=busqueda)|
            Q(resumen__icontains=busqueda)|
            Q(texto__icontains=busqueda)|
            Q(categoria__nombre__icontains=busqueda)
        ).distinct().order_by(ordenar)
    else:
        posts = Post.objects.all().order_by(ordenar)
    
    if categoria and categoria != "Seleccione una categoria":
        posts = posts.filter(
            Q(categoria__nombre__contains=categoria)
        )
    if fecha:
        posts = posts.filter(
            Q(fecha_creacion=fecha)
        )

    posts.order_by('fecha_creacion')
    context={'post':posts, 'cat':cat}

    return render(request, 'index.html', context)

def nosotros(request):

    return render(request, 'nosotros.html',)

def contacto(request):

    return render(request, 'contacto.html',)

def aspirantes(request):

    return render(request, 'aspirantes.html',)

def donacion(request):

    return render(request, 'donacion.html',)

def perfil(request):

    return render(request, 'perfil/perfil.html',)


def crearPost(request):
    
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('blog:index')
    else:
        post_form = PostForm()
    return render(request, 'post/crear_post.html', {'post_form': post_form})

def registrarUsuario(request):
    if request.method == 'POST':
        form= RegistrarForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('blog:index')
        else:
            messages.success(request, f'Error al crear usuario: su contraseña debe contar con numeros, letras y al menos un caracter especial')
    else:
        form = RegistrarForm()

    context = {'form':form}
    return render(request, 'perfil/registro.html', context)