from django.contrib import admin
from .models import Producto, Material, DetalleMaterial
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

admin.site.register(Producto)
admin.site.register(Material)
admin.site.register(DetalleMaterial)
