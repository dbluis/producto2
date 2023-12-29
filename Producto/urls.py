from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     # Usuario
     path("crearUser/", views.crearUser, name="crearUser"),
     path("signout/", views.signout, name="signout"),
     path("signin/", views.signin, name="signin"),
     # Informacion
     path("info/", views.info, name="info"),
     # Materiales
     path("mostrar_materiales/", views.mostrar_materiales,
          name="mostrar_materiales"),
     path("crear_materiales/", views.crear_materiales, name="crear_materiales"),
     # Productos
     path("calcular_costo/<int:producto_id>/",
          views.calcular_costo, name="calcular_costo"),
     path('crear_producto/', views.crear_producto, name='crear_producto'),
     path("mostrar_producto/", views.mostrar_producto, name="mostrar_producto"),

]
