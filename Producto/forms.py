# productos/forms.py
from django import forms
from .models import Material


class Material_unitario(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['nombre', 'cantidad_comprada_gramos', 'costo_total']
