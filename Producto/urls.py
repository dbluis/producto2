from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("crearUser/", views.crearUser, name="crearUser"),
     path("signout/", views.signout, name="signout"),
     path("signin/", views.signin, name="signin"),
     path("info/", views.info, name="info"),
     # Materiales
     path("mostrar_materiales/", views.mostrar_materiales,
          name="mostrar_materiales"),
     path("crear_materiales/", views.crear_materiales, name="crear_materiales"),
     path("mostrar_materiales/<int:material_id>/delete",
          views.eliminar_material, name="eliminar_material"),
     path("mostrar_materiales/<int:material_id>/", views.editar_material, name="editar_material"),
     # Productos
     path("mostrar_producto/", views.mostrar_producto, name="mostrar_producto"),
     path("crear_producto/", views.crear_producto, name="crear_producto"),
     path("calcular_costo/<int:producto_id>/",
          views.calcular_costo, name="calcular_costo"),
     path("mostrar_producto/<int:producto_id>/delete",
          views.eliminar_producto, name="eliminar_producto"),
     path("calcular_costo/<int:producto_id>/", views.detalle, name="detalle")
]