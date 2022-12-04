from django.contrib import admin

# Register your models here.
from .models import *

#Importamos esto para modificar los campos de User de django
from django.contrib.auth.admin import UserAdmin
admin.site.register(Clientes)
admin.site.register(Historial)

#Reemplazmos el modelo de user de django por el nuestro
admin.site.register(CustomUser, UserAdmin)