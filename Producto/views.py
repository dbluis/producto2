from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Material, Producto, DetalleMaterial
from .forms import Material_unitario

# Create your views here.


def index(request):
    return render(request, "index.html")


def crearUser(request):
    if request.method == "GET":
        return render(request, "user/crearUser.html")
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect(index)
            except IntegrityError:
                return render(request, "user/crearUser.html", {"error": "El usuario ya existe"})


def signout(request):
    logout(request)
    return redirect(index)


def signin(request):
    if request.method == "GET":
        return render(request, "user/signin.html")
    else:
        user = authenticate(
            request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "user/signin.html", {"error": "El usuario o contraseña no coinciden"})
        else:
            login(request, user)
            return redirect(index)


def info(request):
    return render(request, "info.html")


def mostrar_materiales(request):
    materiales = Material.objects.all()

    return render(request, "mostrar_materiales.html", {
        "materiales": materiales
    })


def crear_materiales(request):
    if request.method == "GET":
        return render(request, "crear_materiales.html", {
            "form": Material_unitario()
        })
    else:
        try:
            form = Material_unitario(request.POST)
            form.save()
            return redirect("mostrar_materiales")
        except ValueError as e:
            return render(request, "crear_materiales.html", {"error": str(e)})

# Producto


def calcular_costo(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    detalles_materiales = DetalleMaterial.objects.filter(producto=producto)

    costo_total = 0
    for detalle in detalles_materiales:
        cantidad_utilizada = detalle.cantidad_utilizada_gramos
        costo_material = detalle.material.costo_total

        costo_total += (cantidad_utilizada /
                        detalle.material.cantidad_comprada_gramos) * costo_material

    context = {'producto': producto, 'costo_total': costo_total}
    return render(request, 'calcular_costo.html', context)
