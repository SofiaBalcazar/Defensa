from django.urls import path
from .views import Inicio,Registro, Integrantes, Agregar, Modificar, Geolocalizacion

urlpatterns = [
    
    path('Inicio/', Inicio, name='Inicio'), 
    path('registro/', Registro, name="Registro"),
    path('integrantes/', Integrantes, name="integrantes"),
    
    path('agregar/', Agregar, name='Agregar'),
    path('modificar/<int:Codigo>/', Modificar, name='Modificar'),
    path('geolocalizacion/', Geolocalizacion, name='Geolocalizacion'),
]
