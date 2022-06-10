from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myHomeView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html",{})

def usandoPlantilla(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home2.html",{})

def anotherView(*args, **kwargs):
    return HttpResponse('<h2>Solo otra página</h2>')

def jordyPagina(*args, **kwargs):
    return HttpResponse('<h2>PAGINA DE JORDY</h2>')
