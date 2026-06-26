from django.contrib import path
from .views import *

urlpatterns = [
    path('',Home, name='Inicio'), 
    path('registro/',Registro,name="Registro"),
    path('integrantes/',Integrantes,name="integrantes"),
]
