from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'index.html',)

def contacto(request):

    return render(request, 'contacto.html',)

def aspirantes(request):

    return render(request, 'aspirantes.html',)

def nosotros(request):

    return render(request, 'nosotros.html',)

def perfil(request):

    return render(request, 'perfil.html',)