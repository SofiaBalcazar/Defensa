from django.contrib import admin
from .views import *

urlpatterns = [
    path('',home, name='home'),
]
