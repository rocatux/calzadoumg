from django.contrib import admin
from .models import RegistrarFilialModel
from .models import RegistrarTrabajadoresModel
from .models import RegistroExtrasModel
from .models import CalculoSueldoModel

# Register your models here.

admin.site.register(RegistrarFilialModel)
admin.site.register(RegistrarTrabajadoresModel)
admin.site.register(RegistroExtrasModel)
admin.site.register(CalculoSueldoModel)