from django.db import models

class Usuarios(models.Model):
    Codigo = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    contraseña= models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_usuario

class Categorias(models.Model):
    Codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Proveedores(models.Model):
    Codigo = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre_empresa

class Clientes(models.Model):
    Codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Productos(models.Model):
    Codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    # Relaciones (Claves foráneas) apuntando a las tablas correspondientes
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre