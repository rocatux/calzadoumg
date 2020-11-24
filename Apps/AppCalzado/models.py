from django.db import models

# Create your models here.

# modelo para registrar filial

class RegistrarFilialModel (models.Model):
	nombre = models.CharField(max_length=45, null=False)
	telefono = models.IntegerField(null=False)
	email = models.EmailField(max_length=30, null=False)
	tipo_select = ( ('Fabricadora','Fabricadora'),
		       ('Distribuidora y Ventas','Distribuidora y Ventas'),)
	tipo = models.CharField(
		max_length=22,
		choices=tipo_select,
		default= 'Fabricadora',
		)
	direccion = models.CharField(max_length=200, null=False)
	fechaCreacion = models.DateField()

	def __str__(self):
		return '%s / %s'%(self.nombre, self.tipo)


class RegistrarTrabajadoresModel (models.Model):
	nombres = models.CharField(max_length=50, null=False)
	apellidos = models.CharField(max_length=50, null=False)
	telefono = models.IntegerField(null=True, blank=True)
	celular = models.IntegerField(null=False)
	email = models.EmailField(max_length=30, null=False)
	tipo_select = ( ('Trabajador Base','Trabajador Base'),
		       ('Directivo','Directivo'),
		       ('Presidente Directivo','Presidente Directivo'),)
	tipo = models.CharField(
		max_length=30,
		choices=tipo_select,
		default= 'Trabajador Base',
		)
	dpi = models.IntegerField(null=False)
	fechaCreacion = models.DateField()
