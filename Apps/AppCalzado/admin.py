from django.contrib import admin
from .models import RegistrarFilialModel
from .models import RegistrarTrabajadoresModel

# Register your models here.

admin.site.register(RegistrarFilialModel)
admin.site.register(RegistrarTrabajadoresModel)