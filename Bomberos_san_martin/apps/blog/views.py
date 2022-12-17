from django.shortcuts import render, get_object_or_404, redirect

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseNotFound
from django.db.models import Q
from django.contrib import messages

from .models import Post, Categoria, Comentario, Evento, Bombero
from .forms import PostForm, RegistrarForm, ComentarioForm, CategoriaForm, EventoForm, BomberoForm

# Create your views here.
def index(request):
    """ se muestra la pantalla de inicio con post y eventos, además contiene la logica de busqueda y filtros """
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

    eventos= Evento.objects.all().order_by('-fecha_creacion')
    posts.order_by('fecha_creacion')
    context={'post':posts, 'cat':cat, 'eventos':eventos}

    return render(request, 'index.html', context)

def nosotros(request):
    """ se recuperan bomberos y se los muestra por pantalla """
    bomberos = Bombero.objects.all()
    directivos = bomberos.filter(es_directivo=True)
    jefes = bomberos.filter(es_jefe=True)
    bomberos_activos = bomberos.filter(activo=True)
    context={"bomberos":bomberos_activos, "directivos":directivos, "jefes":jefes}
    return render(request, 'nosotros.html', context)

def contacto(request):
    """ se muestra el template con info de contacto """
    return render(request, 'contacto.html',)

def aspirantes(request):
    """ se muestra el template con info para aspirantes """
    return render(request, 'aspirantes.html',)

def donacion(request):
    """ se muestra el template con elementos necesarios para la estacion"""
    return render(request, 'donacion.html',)

def perfil(request):
    """ se muestra info de usuario o enlaces para editar secciones segun permisos """
    return render(request, 'perfil/perfil.html',)

def registrarUsuario(request):
    """ logica de registro de usuario """
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

### CRUD Post

def crearPost(request):
    """ logica para crear post y guardarlo en la base de datos """
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('blog:index')
    else:
        post_form = PostForm()
    return render(request, 'post/guardar_post.html', {'post_form': post_form})

def mostrarPost(request, pk):
    """ se muestra el template con un posteo y sus comentarios """
    post = get_object_or_404(Post, pk=pk)
    comentario_form = ComentarioForm()

    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST or None)
        if comentario_form.is_valid():
            comentario = Comentario()

            comentario.texto = comentario_form.cleaned_data['texto']
            comentario.autor = request.user
            comentario.id_post = post

            print(comentario.id_post)
            comentario.save()
            comentario_form = ComentarioForm()
            #return redirect('blog:mostrar_post'+'/'+str(pk))

    comentarios = Comentario.objects.filter(
        Q(id_post=pk)
        ).order_by('-fecha_creacion')
    context ={'post':post, 'comentarios':comentarios, 'comentario_form':comentario_form}
    return render(request, 'post/mostrar_post.html', context)

def administrarPosts(request):
    """ se muestran los post creados con las opciones de editar, eliminar y crear """
    cat= Categoria.objects.all()
    posts = Post.objects.all().order_by('-fecha_creacion')
    context={'post':posts, 'cat':cat}
    return render(request, 'post/administrar_post.html', context)

def actualizarPost(request,pk):
    """ funcion para modificar un post creado """
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post.titulo=post_form.cleaned_data['titulo']
            post.resumen=post_form.cleaned_data['resumen']
            post.resumen=post_form.cleaned_data['resumen']
            post.texto=post_form.cleaned_data['texto']
            post.imagen=post_form.cleaned_data['imagen']
            post.categoria=post_form.cleaned_data['categoria']
            post.usuario=post_form.cleaned_data['usuario']
            
            post.save()
            messages.success(request, f"Post: '{post.titulo}' actualizado")

            return redirect('blog:administrar_posts')
    else:
        post_form = PostForm(initial={'titulo':post.titulo, 'resumen':post.resumen, 'texto':post.texto, 'imagen':post.imagen, 'categoria':post.categoria, 'usuario':post.usuario})

    context = {'post_form': post_form}
    return render(request, 'post/guardar_post.html', context)

def eliminarPost(request,pk):
    """ funcion para eliminar un post de la base de datos """
    post = get_object_or_404(Post, pk=pk)
    print("Post eliminado: ",post)
    post.delete()
    return redirect('blog:administrar_posts')

### CRUD Categoria

def administrarCategorias(request):
    """ se muestran las categorias creadas con las opciones de editar, eliminar y crear """
    categorias= Categoria.objects.all()
    context={'categorias':categorias}
    return render(request, 'categoria/administrar_categorias.html', context)

def agregarCategoria(request):
    """ toma los compos del form para crear una categoria y guardarla en la base de datos """
    if request.method == 'POST':
        categoria_form = CategoriaForm(request.POST or None)
        if categoria_form.is_valid():
            categoria_form.save()
            messages.success(request, f"Categoria: '{categoria_form.cleaned_data['nombre']}' creada.")
            return redirect('blog:administrar_categorias')
    else:
        categoria_form = CategoriaForm()
    context={'categoria_form': categoria_form}
    return render(request, 'categoria/guardar_categoria.html', context)

def actualizarCategoria(request,pk):
    """ recupera la categoria por su id y actualiza los campos modificados """
    categoria = get_object_or_404(Categoria, pk=pk)
    
    if request.method == 'POST':
        categoria_form = CategoriaForm(request.POST or None)
        if categoria_form.is_valid():
            categoria.nombre=categoria_form.cleaned_data['nombre']

            categoria.save()
            messages.success(request, f"Categoria: '{categoria.nombre}' actualizada.")
            return redirect('blog:administrar_categorias')
    else:
        categoria_form = CategoriaForm(initial={'nombre':categoria.nombre})

    context = {'categoria_form': categoria_form}
    return render(request, 'categoria/guardar_categoria.html', context)

def eliminarCategoria(request,pk):
    """ recupera la categoria por su id y la elimina """
    categoria = get_object_or_404(Categoria, pk=pk)
    print("Categoria eliminada: ",categoria)
    nombre_categoria = categoria.nombre
    categoria.delete()
    messages.success(request, f"Categoria '{nombre_categoria}' eliminada.")
    return redirect('blog:administrar_categorias')

### CRUD Evento

def administrarEventos(request):
    """ se muestran las categorias creadas con las opciones de editar, eliminar y crear """
    eventos= Evento.objects.all()
    context={'eventos':eventos}
    return render(request, 'evento/administrar_eventos.html', context)

def agregarEvento(request):
    """ toma los compos del form para crear un evento y guardarlo en la base de datos """
    if request.method == 'POST':
        evento_form = EventoForm(request.POST or None)
        if evento_form.is_valid():
            evento_form.save()
            messages.success(request, f"Nuevo evento creado: '{evento_form.cleaned_data['titulo']}'.")
            return redirect('blog:administrar_eventos')
    else:
        evento_form = EventoForm()
    context={'evento_form': evento_form}
    return render(request, 'evento/guardar_evento.html', context)

def actualizarEvento(request,pk):
    """ recupera el evento por id y actualiza los campos modificados """
    evento = get_object_or_404(Evento, pk=pk)
    
    if request.method == 'POST':
        evento_form = EventoForm(request.POST or None)
        if evento_form.is_valid():
            evento.titulo=evento_form.cleaned_data['titulo']
            evento.descripcion=evento_form.cleaned_data['descripcion']

            evento.save()
            messages.success(request, f"Evento '{evento.nombre}' actualizado.")
            return redirect('blog:administrar_eventos')
    else:
        evento_form = EventoForm(initial={'titulo':evento.titulo, 'descripcion':evento.descripcion})

    context = {'evento_form': evento_form}
    return render(request, 'evento/guardar_evento.html', context)

def eliminarEvento(request,pk):
    """ recupera el evento por su id y lo elimina de la base de datos"""
    evento = get_object_or_404(Evento, pk=pk)
    print("Evento eliminado: ",evento)
    nombre_evento = evento.titulo
    evento.delete()
    messages.success(request, f"Evento '{nombre_evento}' eliminado.")
    return redirect('blog:administrar_eventos')

### CRUD Bombero

def administrarBomberos(request):
    """ se muestran los bomberos creados con las opciones de editar, eliminar y crear """
    bomberos= Bombero.objects.all()
    directivos = bomberos.filter(es_directivo=True)
    jefes = bomberos.filter(es_jefe=True)
    bomberos_activos = bomberos.filter(activo=True)
    context={"bomberos":bomberos_activos, "directivos":directivos, "jefes":jefes}
    return render(request, 'bombero/administrar_bomberos.html', context)

def agregarBombero(request):
    """ toma los compos del form para crear un bombero y guardarlo en la base de datos """
    if request.method == 'POST':
        bombero_form = BomberoForm(request.POST or None, request.FILES or None)
        if bombero_form.is_valid():
            print('llegue')
            bombero_form.save()
            messages.success(request, f"Nuevo bombero creado: '{bombero_form.cleaned_data['apellido']}, {bombero_form.cleaned_data['primer_nombre']} {bombero_form.cleaned_data['segundo_nombre']}'.")
            return redirect('blog:administrar_bomberos')
    else:
        bombero_form = BomberoForm()
    context={'bombero_form': bombero_form}
    return render(request, 'bombero/guardar_bombero.html', context)

def actualizarBombero(request,pk):
    """ recupera el bombero por id y actualiza los campos modificados """
    bombero = get_object_or_404(Bombero, pk=pk)
    
    if request.method == 'POST':
        bombero_form = BomberoForm(request.POST or None, request.FILES or None, instance=bombero)
        if bombero_form.is_valid():
            # bombero.primer_nombre=bombero_form.cleaned_data['primer_nombre']
            # bombero.segundo_nombre=bombero_form.cleaned_data['segundo_nombre']
            # bombero.apellido=bombero_form.cleaned_data['apellido']
            # bombero.fecha_nacimiento=bombero_form.cleaned_data['fecha_nacimiento']
            # bombero.imagen=bombero_form.cleaned_data['imagen']
            # bombero.biografia=bombero_form.cleaned_data['biografia']
            # bombero.activo=bombero_form.cleaned_data['activo']
            # bombero.es_jefe=bombero_form.cleaned_data['es_jefe']
            # bombero.es_directivo=bombero_form.cleaned_data['es_directivo']
            
            bombero.save()
            messages.success(request, f"Bombero '{bombero.apellido}, {bombero.primer_nombre} {bombero.segundo_nombre}' actualizado.")
            return redirect('blog:administrar_bomberos')
    else:
        bombero_form = BomberoForm(instance=bombero)

    context = {'bombero_form': bombero_form}
    return render(request, 'bombero/guardar_bombero.html', context)

def eliminarBombero(request,pk):
    """ recupera el bombero por su id y lo elimina de la base de datos"""
    bombero = get_object_or_404(Bombero, pk=pk)
    print("Bombero eliminado: ",bombero)
    nombre_bombero = bombero.primer_nombre + bombero.segundo_nombre
    apellido_bombero = bombero.apellido
    bombero.delete()
    messages.success(request, f"Bombero '{apellido_bombero}, {nombre_bombero}' eliminado.")
    return redirect('blog:administrar_bomberos')