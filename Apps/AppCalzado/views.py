from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.views.generic import TemplateView, FormView, CreateView, ListView, DeleteView, UpdateView

from .forms import CrearFilialForm, CrearTrabajadoresForm, RegistrarUsuarioForm, CrearHorasExtrasForm, CrearHorasExtrasForm2
from .forms import CalculoSueldoForm
from .models import RegistrarFilialModel, RegistrarTrabajadoresModel, RegistroExtrasModel, CalculoSueldoModel

# Create your views here.



#clases de inicio--------------------------------------------------------------------

class IndexView(TemplateView):
	template_name='inicio.html'

#modelos filiales---------------------------------------------------------------------

class RegistrarFilialView(CreateView):
	template_name='registrarfilial.html'
	form_class=CrearFilialForm
	success_url=reverse_lazy('appCalzado:registrosFiliales')

class ListaFilialesView(ListView):
	template_name = 'listafiliales.html'
	model = RegistrarFilialModel
	paginate_by = 6

	def get_queryset(self):
		return RegistrarFilialModel.objects.all().order_by('id')

class EliminarFilialView(DeleteView):
	model = RegistrarFilialModel
	template_name = 'eliminar_filial.html'
	success_url = reverse_lazy('appCalzado:registrosFiliales')

class EditarFilialView(UpdateView):
	model = RegistrarFilialModel
	form_class = CrearFilialForm
	template_name = 'editar_filial.html'
	success_url = reverse_lazy('appCalzado:registrosFiliales')

#modelos trabajadores----------------------------------------------------------------

class RegistrarTrabajadoresView(CreateView):
	template_name='registrar_trabajadores.html'
	form_class=CrearTrabajadoresForm
	success_url=reverse_lazy('appCalzado:registrosTrabajadores')

class ListaTrabajadoresView(ListView):
	template_name = 'lista_trabajadores.html'
	model = RegistrarTrabajadoresModel
	paginate_by = 6

	def get_queryset(self):
		return RegistrarTrabajadoresModel.objects.all().order_by('id')

class EliminarTrabajadorView(DeleteView):
	model = RegistrarTrabajadoresModel
	template_name = 'eliminar_trabajador.html'
	success_url = reverse_lazy('appCalzado:registrosTrabajadores')

class EditarTrabajadorView(UpdateView):
	model = RegistrarTrabajadoresModel
	form_class = CrearTrabajadoresForm
	template_name = 'editar_trabajador.html'
	success_url = reverse_lazy('appCalzado:registrosTrabajadores')

#clase login metodo logout---------------------------------------------------------------

class LoginView(FormView):
	template_name='login.html'
	form_class = AuthenticationForm
	success_url = reverse_lazy('appCalzado:inicio')

	def form_valid (self, form):
		login(self.request, form.get_user())
		return super (LoginView, self) .form_valid (form)

def logoutview(request):
	logout(request)
	return redirect ('appCalzado:login')

#modelos para creacion de usuario---------------------------------------------------------

class RegistrarUsuarioView(CreateView):
    model = User
    template_name='crear_usuario.html'
    form_class= RegistrarUsuarioForm
    success_url = reverse_lazy('appCalzado:listaUsuario')

class ListaUsuarioView(ListView):
	template_name = 'lista_usuario.html'
	model = User
	paginate_by = 6

	def get_queryset(self):
		return User.objects.all().order_by('id')

class EliminarUsuarioView(DeleteView):
	model = User
	template_name = 'eliminar_usuario.html'
	success_url = reverse_lazy('appCalzado:listaUsuario')

class EditarUsuarioView(UpdateView):
	model = User
	form_class = RegistrarUsuarioForm
	template_name = 'editar_usuario.html'
	success_url = reverse_lazy('appCalzado:listaUsuario')

#modelo para registro de horas extras----------------------------------------------------

class RegistrarHorasExtrasView(CreateView):
    model = RegistroExtrasModel
    template_name='registrar_horasextras.html'
    form_class= CrearHorasExtrasForm
    success_url = reverse_lazy('appCalzado:registrosHorasExtras')

class RegistrosDeHorasExtrasView(ListView):
	template_name = 'lista_horasextras.html'
	model = RegistroExtrasModel
	paginate_by = 6

	def get_queryset(self):
		return RegistroExtrasModel.objects.all().order_by('id')

class EliminarRegistroHExtrasView(DeleteView):
	model = RegistroExtrasModel
	template_name = 'eliminar_registrosextras.html'
	success_url = reverse_lazy('appCalzado:registrosHorasExtras')

class EditarHorasExtrasView(UpdateView):
	model = RegistroExtrasModel
	form_class = CrearHorasExtrasForm2
	template_name = 'editar_horasextras.html'
	success_url = reverse_lazy('appCalzado:registrosHorasExtras')

#404-------------------------------------------------------------------------------------

def error_404_view(request,exception):
	return render(request,'404.html')


#Calculo sueldo y registro---------------------------------------------------------------

class CalculoSueldoView(CreateView):
    model = CalculoSueldoModel
    template_name='calculosueldo.html'
    form_class= CalculoSueldoForm
    success_url = reverse_lazy('appCalzado:registrosSueldos')

class RegistrosSueldosView(ListView):
	template_name = 'lista_sueldos.html'
	model = CalculoSueldoModel
	paginate_by = 6

	def get_queryset(self):
		return CalculoSueldoModel.objects.all().order_by('id')

class EliminarSueldoView(DeleteView):
	model = CalculoSueldoModel
	template_name = 'eliminar_sueldo.html'
	success_url = reverse_lazy('appCalzado:registrosSueldos')

class EditarSueldoView(UpdateView):
	model = CalculoSueldoModel
	form_class = CalculoSueldoForm
	template_name = 'editar_sueldo.html'
	success_url = reverse_lazy('appCalzado:registrosSueldos')

