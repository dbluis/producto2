from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("crearUser/", views.crearUser, name="crearUser"),
    path("signout/", views.signout, name="signout"),
    path("signin/", views.signin, name="signin"),
    path("info/", views.info, name="info"),
    path("mostrar_materiales/", views.mostrar_materiales,
         name="mostrar_materiales"),
    path("crear_materiales/", views.crear_materiales, name="crear_materiales"),
    path("calcular_costo/<int:producto_id>/",
         views.calcular_costo, name="calcular_costo")

]
