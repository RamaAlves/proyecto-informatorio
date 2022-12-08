from django.shortcuts import render, redirect

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseNotFound

from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):

    return render(request, 'index.html',)

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
    post_form = PostForm()
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            print(post_form)
            return redirect('index')
    else:
        post_form = PostForm()
    return render(request, 'post/crear_post.html', {'post_form': post_form})