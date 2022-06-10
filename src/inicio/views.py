from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myHomeView(*args, **kwargs):
    return HttpResponse('<h1>HOLA MUNDO DESDE DJANDO EN VIEWS.PY</h1>')

def anotherView(*args, **kwargs):
    return HttpResponse('<h2>Solo otra página</h2>')

def jordyPagina(*args, **kwargs):
    return HttpResponse('<h2>PAGINA DE JORDY</h2>')
