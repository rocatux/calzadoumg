"""calzadoumg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from .views import *

app_name="appCalzado" 

urlpatterns = [
#inicio
path('inicio/', login_required(IndexView.as_view()), name= 'inicio'),

#resgistrar
path('RegistrarFilial/', login_required(RegistrarFilialView.as_view()), name= 'registrarFilial'),
path('RegistrarTrabajador/', login_required(RegistrarTrabajadoresView.as_view()), name= 'registrarTrabajador'),
path('RegistrarUsuario/', login_required(RegistrarUsuarioView.as_view()), name='registrarUsuario'),
path('RegistrarHorasExtras/', login_required(RegistrarHorasExtrasView.as_view()), name='registrarHorasExtras'),
path('CalculoSueldo/', login_required(CalculoSueldoView.as_view()), name='calculoSueldo'),

#registros
path('RegistrosFiliales/', login_required(ListaFilialesView.as_view()), name= 'registrosFiliales'),
path('RegistrosTrabajadores/', login_required(ListaTrabajadoresView.as_view()), name= 'registrosTrabajadores'),
path('ListaUsuarios/', login_required(ListaUsuarioView.as_view()), name='listaUsuario'),
path('RegistrosHorasExtras/', login_required(RegistrosDeHorasExtrasView.as_view()), name='registrosHorasExtras'),
path('RegistrosSueldos/', login_required(RegistrosSueldosView.as_view()), name='registrosSueldos'),

#eliminarregistros
path('EliminarFilial/<int:pk>/',login_required(EliminarFilialView.as_view()), name='eliminarFilial'),
path('EliminarTrabajador/<int:pk>/',login_required(EliminarTrabajadorView.as_view()), name='eliminarTrabajador'),
path('EliminarUsuario/<int:pk>/',login_required(EliminarUsuarioView.as_view()), name='eliminarUsuario'),
path('EliminarHorasExtras/<int:pk>/',login_required(EliminarRegistroHExtrasView.as_view()), name='eliminarHorasExtras'),
path('EliminarSueldos/<int:pk>/',login_required(EliminarSueldoView.as_view()), name='eliminarSueldo'),


#editar
path('EditarFilial/<int:pk>/',login_required(EditarFilialView.as_view()), name='editarFilial'),
path('EditarTrabajador/<int:pk>/',login_required(EditarTrabajadorView.as_view()), name='editarTrabajador'),
path('EditarUsuario/<int:pk>/',login_required(EditarUsuarioView.as_view()), name='editarUsuario'),
path('EditarHorasExtras<int:pk>/',login_required(EditarHorasExtrasView.as_view()), name='editarHorasExtras'),
path('EditarSueldo<int:pk>/',login_required(EditarSueldoView.as_view()), name='editarSueldo'),
]
