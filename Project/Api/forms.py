from django import forms
from .models import Productos

class FormularioProductos(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__' # Mapea automáticamente todas las columnas del modelo

    # Validación extra requerida por el TP para asegurar tipos de datos coherentes
    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            raise forms.ValidationError("El stock no puede ser un número negativo.")
        return stock