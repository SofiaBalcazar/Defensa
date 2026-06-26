from django.contrib import admin
from .models import Usuarios, Categorias, Proveedores, Clientes, Productos

# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Categorias)
admin.site.register(Proveedores)
admin.site.register(Clientes)
admin.site.register(Productos)