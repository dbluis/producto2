# productos/forms.py
from django import forms
from .models import Material, Producto, DetalleMaterial, Clientes


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion']

class DetalleMaterialForm(forms.ModelForm):
    class Meta:
        model = DetalleMaterial
        fields = ['material', 'cantidad_utilizada_gramos']

class Material_unitario(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['nombre', 'cantidad_comprada_gramos', 'costo_total']

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre', 'apellido', 'telefono', 'direccion']