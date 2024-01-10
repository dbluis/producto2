# productos/forms.py
from django import forms
from .models import Material, Producto, DetalleMaterial, Clientes


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={"class": "form-control", "placeholder": "Escribe un nombre"}),
            'descripcion': forms.Textarea(attrs={"class": "form-control", "placeholder": "Escribe una descripcion"}),
        }


class DetalleMaterialForm(forms.ModelForm):
    class Meta:
        model = DetalleMaterial
        fields = ['material', 'cantidad_utilizada_gramos']
        widgets = {
            'material': forms.Select(attrs={"class": "form-control"}),
            'cantidad_utilizada_gramos': forms.NumberInput(attrs={"class": "form-control"}),
        }
        labels = {
            'cantidad_utilizada_gramos': 'Cantidad a usar:', 'material': 'Selecciona un material:'
        }


class Material_unitario(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['nombre', 'cantidad_comprada_gramos', 'costo_total']
        widgets = {
            'nombre': forms.TextInput(attrs={"class": "form-control", "placeholder": "Escribe un nombre"}),
            'cantidad_comprada_gramos': forms.TextInput(attrs={"class": "form-control", "placeholder": "Escribe la cantidad comprada"}),
            'costo_total': forms.TextInput(attrs={"class": "form-control", "placeholder": "Escribe el costo total"}),
        }
        labels = {
            # Cambia 'Cantidad' al texto que desees
            'cantidad_comprada_gramos': 'Cantidad',
        }


class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre', 'apellido', 'telefono', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={"class": "form-control", "placeholder": "Escribe un nombre"}),
            'apellido': forms.TextInput(attrs={"class": "form-control", "placeholder": "Escribe un apellido"}),
            "telefono": forms.TextInput(attrs={"class": "form-control", "placeholder": "Escribe un telefono"}),
            "direccion": forms.TextInput(attrs={"class": "form-control", "placeholder": "Escribe una direccion"}),
        }
