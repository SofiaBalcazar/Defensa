from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FormularioProductos

# Vista Segura para crear productos usando tu formulario
@login_required
def crear_producto_seguro(request):
    if request.method == 'POST':
        form = FormularioProductos(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
    else:
        form = FormularioProductos()
    
    return render(request, 'gestion/crear_producto.html', {'form': form})

# Vista de Geolocalización (Triangulación)
PUNTO_A = {'x': 0, 'y': 0}
PUNTO_B = {'x': 100, 'y': 0}
PUNTO_C = {'x': 50, 'y': 86.6}

@login_required
def calcular_triangulacion(request):
    resultado = None
    if request.method == 'POST':
        distancia_a = float(request.POST.get('distancia_a', 0))
        distancia_b = float(request.POST.get('distancia_b', 0))
        distancia_c = float(request.POST.get('distancia_c', 0))
        
        # Trilateración matemática
        x = (distancia_a**2 - distancia_b**2 + PUNTO_B['x']**2) / (2 * PUNTO_B['x'])
        y = (distancia_a**2 - distancia_c**2 + PUNTO_C['x']**2 + PUNTO_C['y']**2 - 2 * PUNTO_C['x'] * x) / (2 * PUNTO_C['y'])
        
        resultado = {'x': round(x, 2), 'y': round(y, 2)}

    contexto = {
        'punto_a': PUNTO_A, 'punto_b': PUNTO_B, 'punto_c': PUNTO_C, 'resultado': resultado
    }
    return render(request, 'gestion/geolocalizacion.html', contexto)