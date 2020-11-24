from django import forms
from datetime import datetime
from django.forms import *

from .models import RegistrarFilialModel, RegistrarTrabajadoresModel

# creacion de forms

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
	    }