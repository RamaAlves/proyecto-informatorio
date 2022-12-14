from django.shortcuts import render, get_object_or_404, redirect

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseNotFound
from django.db.models import Q
from django.contrib import messages

from .models import Post, Categoria, Comentario, Bomberos
from .forms import PostForm, RegistrarForm, ComentarioForm

# Create your views here.
def index(request):
    cat= Categoria.objects.all()

    ordenar = request.GET.get('ordenar')
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

def mostrarPost(request, id):
    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST or None)
        if comentario_form.is_valid():
            comentario_form.save()
            return redirect(f'post/mostrar_post.html/{id}')
    else:
        comentario_form = PostForm()

    post = get_object_or_404(Post, id=id)
    comentarios = get_object_or_404(Comentario, id_post=id)
    context ={'post':post, 'comentarios':comentarios}
    return render(request, 'post/mostrar_post.html', context)

def nosotros(request):
    bomberos = Bomberos.objects.all()
    directivos = bomberos.filter(es_directivo=True)
    jefes = bomberos.filter(es_jefe=True)
    bomberos_activos = bomberos.filter(activo=True)
    context={"bomberos":bomberos_activos, "directivos":directivos, "jefes":jefes}
    return render(request, 'nosotros.html', context)

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
    return render(request, 'post/guardar_post.html', {'post_form': post_form})

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