from django.contrib import admin
from .models import Usuario, Categoria, Proveedor, Cliente, Producto

# ABM y Consultas para Usuarios
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_usuario', 'email') # Consulta: columnas a mostrar
    search_fields = ('nombre_usuario', 'email') # Consulta: buscador obligatorio

# ABM y Consultas para Categorías
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

# ABM y Consultas para Proveedores
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre_empresa', 'telefono', 'email')
    search_fields = ('nombre_empresa',)

# ABM y Consultas para Clientes
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'email')
    search_fields = ('nombre', 'apellido', 'dni')

# ABM y Consultas para Productos
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria', 'proveedor')
    list_filter = ('categoria', 'proveedor') # Consulta: filtros laterales
    search_fields = ('nombre',)