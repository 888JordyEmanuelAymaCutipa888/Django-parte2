"""viajes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio.views import myHomeView
from inicio.views import anotherView 
from inicio.views import jordyPagina 
from inicio.views import usandoPlantilla 

urlpatterns = [
    path('usandoPlantilla/', usandoPlantilla),
    path('jordy/', jordyPagina, name='Página de Jordy'),
    path('another/', anotherView),
    path('', myHomeView, name='Página de Inicio'),
    path('admin/', admin.site.urls),
]
