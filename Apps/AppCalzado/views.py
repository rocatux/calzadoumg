from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.views.generic import TemplateView, FormView

# Create your views here.

#clases de inicio-------------------------------------------------

class IndexView(TemplateView):
	template_name='inicio.html'

#clase login metodo logout-----------------------------------------

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

