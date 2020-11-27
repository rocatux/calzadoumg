from django import forms
from datetime import datetime
from django.forms import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import RegistrarFilialModel, RegistrarTrabajadoresModel, RegistroExtrasModel

# creacion de forms

class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name','email', 'password1', 'password2']

        widgets = {

        'username': TextInput(attrs={'class': 'form-control', 'id': 'username', 'autocomplete':'off'}),
        'first_name': TextInput(attrs={'class': 'form-control', 'id': 'first_name', 'autocomplete':'off'}),
        'last_name': TextInput(attrs={'class': 'form-control', 'id': 'last_name', 'autocomplete':'off'}),
        'email': TextInput(attrs= {'class': 'form-control','placeholder': 'email','autocomplete' : "off",}),
        'password1': PasswordInput(attrs={'class': 'form-control', 'id':'password1', 'type':'password'}),
        'password2': PasswordInput(attrs={'class': 'form-control'}),
        
        }

class CrearFilialForm(ModelForm):
	class Meta:
		model = RegistrarFilialModel 
		fields = '__all__'

		widgets = {
		'nombre': TextInput(attrs= {'class': 'form-control', 'placeholder': 'nombre','autocomplete' : "off",}),
	    'telefono': TextInput(attrs= {'class': 'form-control',  'maxlength':'8', 'placeholder': '# telefono','autocomplete' : "off",}),
	    'email': TextInput(attrs= {'class': 'form-control','placeholder': 'email','autocomplete' : "off",}),
	    'tipo': Select(attrs= {'class': 'form-control m-bot15',}),
	    'direccion': TextInput(attrs= {'class': 'form-control','placeholder': 'direccion','autocomplete' : "off",}),
	    'fechaCreacion': DateInput(format='%Y-%m-%d', attrs= {'readonly': True,'class': 'form-control','value': datetime.now().strftime('%Y-%m-%d'),}),
	    }

class CrearTrabajadoresForm(ModelForm):
	class Meta:
		model = RegistrarTrabajadoresModel 
		fields = '__all__'

		widgets = {
		'nombres': TextInput(attrs= {'class': 'form-control', 'placeholder': 'nombres','autocomplete' : "off",}),
		'apellidos': TextInput(attrs= {'class': 'form-control', 'placeholder': 'apellidos','autocomplete' : "off",}),
	    'telefono': TextInput(attrs= {'class': 'form-control',  'maxlength':'8', 'placeholder': '# telefono','autocomplete' : "off",}),
	    'celular': TextInput(attrs= {'class': 'form-control',  'maxlength':'8', 'placeholder': '# celular','autocomplete' : "off",}),
	    'email': TextInput(attrs= {'class': 'form-control','placeholder': 'email','autocomplete' : "off",}),
	    'tipo': Select(attrs= {'class': 'form-control m-bot15',}),
	    'dpi': TextInput(attrs= {'class': 'form-control','placeholder': 'dpi','autocomplete' : "off",}),
	    'fechaCreacion': DateInput(format='%Y-%m-%d', attrs= {'readonly': True,'class': 'form-control','value': datetime.now().strftime('%Y-%m-%d'),}),
	    'filialBase': Select(attrs= {'class': 'form-control m-bot15',}),
	    'sueldo': NumberInput(attrs= {'class': 'form-control', 'autocomplete' : "off",}),
	    }

class CrearHorasExtrasForm(ModelForm):
	class Meta:
		model = RegistroExtrasModel 
		fields = '__all__'

		widgets = {
		'motivo': TextInput(attrs= {'class': 'form-control', 'placeholder': 'escriba descripcion','autocomplete' : "off",}),
		'fecha': DateInput(attrs= {'readonly': True,'class': 'form-control','placeholder': 'fecha',}),
		'cantidadHorasExtras':NumberInput(attrs= {'class': 'form-control',  'maxlength':'6', 'autocomplete' : "off",}),
		'trabajador': Select(attrs= {'class': 'form-control m-bot15',}),
		'filialExtras': Select(attrs= {'class': 'form-control m-bot15',}),
		}

#form secundario para edicion de datos
class CrearHorasExtrasForm2(ModelForm):
	class Meta:
		model = RegistroExtrasModel 
		fields = '__all__'

		widgets = {
		'motivo': TextInput(attrs= {'class': 'form-control', 'placeholder': 'escriba descripcion','autocomplete' : "off",}),
		'fecha': DateInput(attrs= {'readonly': True,'class': 'form-control','placeholder': 'fecha',}),
		'cantidadHorasExtras':NumberInput(attrs= {'class': 'form-control',  'maxlength':'6', 'autocomplete' : "off",}),
		'trabajador': Select(attrs= {'readonly':'readonly', 'class': 'form-control m-bot15',}),
		'filialExtras': Select(attrs= {'class': 'form-control m-bot15',}),
		}