from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import FormularioProductos
from .models import Productos

# ==========================================
# 🏛️ TUS VISTAS ORIGINALES (¡Recuperadas!)
# ==========================================

def Inicio(request):
    # Trae los últimos 3 productos insertados
    query = Productos.objects.all().order_by('-Codigo')[:3]
    data = {
        'Tabla': query
    }
    return render(request, 'Base.html', data)

def Registro(request):
    # Aquí va tu lógica actual de Registro (si usas formulario, ponlo en data)
    data = {}
    return render(request, 'Pages/Registro.html', data)

def Integrantes(request):
    data = {}
    return render(request, 'Pages/Integrantes.html', data)


# ==========================================
# 🛡️ VISTAS DE PRODUCTOS (CON CONTROL DE ACCESO)
# ==========================================

@login_required # Candado de seguridad
def Agregar(request):
    data = {
        'Formulario': FormularioProductos()
    }
    if request.method == 'POST':
        query = FormularioProductos(data=request.POST, files=request.FILES)
        if query.is_valid():
            query.save()
            data['mensaje'] = 'Datos Registrados'
        else:
            data['Formulario'] = FormularioProductos()
    return render(request, 'Pages/Agregar.html', data)

@login_required # Candado de seguridad
def Modificar(request, Codigo):
    query = get_object_or_404(Productos, Codigo=Codigo)
    data = {
        'Formulario': FormularioProductos(instance=query)
    }
    if request.method == 'POST':
        query = FormularioProductos(data=request.POST, instance=query, files=request.FILES)
        if query.is_valid():
            query.save()
            data['mensaje'] = 'Datos Modificados'
            return redirect('Inicio')
        else:
            data['Formulario'] = FormularioProductos()
    return render(request, 'Pages/Modificar.html', data)


# ==========================================
# 📍 MÓDULO DE GEOLOCALIZACIÓN Y TRIANGULACIÓN
# ==========================================

# Coordenadas fijas de las 3 Antenas de referencia
PUNTO_A = {'x': 0, 'y': 0}
PUNTO_B = {'x': 100, 'y': 0}
PUNTO_C = {'x': 50, 'y': 86.6}

@login_required
def Geolocalizacion(request):
    data = {
        'punto_a': PUNTO_A,
        'punto_b': PUNTO_B,
        'punto_c': PUNTO_C,
        'resultado': None
    }
    
    if request.method == 'POST':
        distancia_a = float(request.POST.get('distancia_a', 0))
        distancia_b = float(request.POST.get('distancia_b', 0))
        distancia_c = float(request.POST.get('distancia_c', 0))
        
        # Algoritmo matemático de trilateración para calcular ubicación aproximada
        x = (distancia_a**2 - distancia_b**2 + PUNTO_B['x']**2) / (2 * PUNTO_B['x'])
        y = (distancia_a**2 - distancia_c**2 + PUNTO_C['x']**2 + PUNTO_C['y']**2 - 2 * PUNTO_C['x'] * x) / (2 * PUNTO_C['y'])
        
        data['resultado'] = {
            'x': round(x, 2),
            'y': round(y, 2)
        }
        
    return render(request, 'Pages/Geolocalizacion.html', data)