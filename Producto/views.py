from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Material, Producto, DetalleMaterial, Clientes
from .forms import Material_unitario, ProductoForm, DetalleMaterialForm, ClientesForm
from django.forms import formset_factory


def index(request):
    return render(request, "index.html")


# Usuario
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

# Texto
def info(request):
    return render(request, "info.html")


# Materiales
@login_required
def mostrar_materiales(request):
    materiales = Material.objects.all()

    return render(request, "mostrar_materiales.html", {
        "materiales": materiales
    })

@login_required
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

@login_required
def editar_material(request, material_id):
    material_unico = get_object_or_404(Material, pk=material_id)

    if request.method == "GET":
        form = Material_unitario(instance=material_unico)
        return render(request, "editar_material.html", {"material": material_unico, "form": form})
    elif request.method == "POST":
        try:
            form = Material_unitario(request.POST, instance=material_unico)
            if form.is_valid():
                form.save()
                return redirect("mostrar_materiales")
            else:
                # Manejar caso en el que el formulario no es válido
                return render(request, "editar_material.html", {"material": material_unico, "form": form})
        except Exception as e:
            # Manejar otras excepciones si es necesario
            return render(request, "editar_material.html", {"error": str(e)})

@login_required
def eliminar_material(request, material_id):
    material = get_object_or_404(Material, pk=material_id)
    if request.method == "POST":
        material.delete()
        return redirect("mostrar_materiales")


# Producto
@login_required
def crear_producto(request):
    try:
        material = Material.objects.all()
        DetalleMaterialFormSet = formset_factory(
            DetalleMaterialForm, extra=len(material))

        if request.method == 'POST':
            producto_form = ProductoForm(request.POST)
            detalle_formset = DetalleMaterialFormSet(
                request.POST, prefix='detalle')

            if producto_form.is_valid() and detalle_formset.is_valid():
                producto = producto_form.save()
                for detalle_form in detalle_formset:
                    detalle = detalle_form.save(commit=False)
                    detalle.producto = producto
                    detalle.save()

                return redirect('calcular_costo', producto_id=producto.id)
        else:
            producto_form = ProductoForm()
            detalle_formset = DetalleMaterialFormSet(prefix='detalle')

        context = {'producto_form': producto_form,
                   'detalle_formset': detalle_formset}
        return render(request, 'crear_producto.html', context)
    except ValueError as e:
        return render(request, "crear_producto.html", {"error": str(e)})

@login_required
def calcular_costo(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    detalles_materiales = DetalleMaterial.objects.filter(producto=producto)

    costo_total = 0
    for detalle in detalles_materiales:
        cantidad_utilizada = detalle.cantidad_utilizada_gramos
        costo_material = detalle.material.costo_total

        costo_total += (cantidad_utilizada /
                        detalle.material.cantidad_comprada_gramos) * costo_material
    costo_total = round(costo_total, 2)

    context = {'producto': producto, 'costo_total': costo_total}
    return render(request, 'calcular_costo.html', context)

@login_required
def mostrar_producto(request):
    productos = Producto.objects.all()

    return render(request, "mostrar_producto.html", {
        "productos": productos
    })

@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == "POST":
        producto.delete()
        return redirect("mostrar_producto")

@login_required
def detalle(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == "POST":
        return redirect("calcular_costo")


# Clientes
@login_required
def crear_cliente(request):
    if request.method == "GET":
        return render(request, "clientes/crear_cliente.html", {
            "form": ClientesForm()
        })
    else:
        try:
            form = ClientesForm(request.POST)
            form.save()
            return redirect("mostrar_clientes")
        except ValueError as e:
            return render(request, "clientes/mostrar_clientes.html", {"error": str(e)})
@login_required
def mostrar_clientes(request):
    clientes = Clientes.objects.all()

    return render(request, "clientes/mostrar_clientes.html", {
        "clientes": clientes
    })
@login_required
def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Clientes, pk=cliente_id)
    if request.method == "POST":
        cliente.delete()
        return redirect("mostrar_clientes")
@login_required
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Clientes, pk=cliente_id)
    if request.method == "GET":
        form = ClientesForm(instance=cliente)
        return render(request, "clientes/editar_cliente", {
            "cliente": cliente, "form":form
        })
    elif request.method == "POST":
        try:
            form = ClientesForm(request.POST ,instance=cliente)
            if form.is_valid():
                form.save()
                return redirect("mostrar_clientes")
            else:
                # Manejar caso en el que el formulario no es válido
                return render(request, "clientes/editar_cliente.html", {"cliente": cliente, "form": form})
        except ValueError as e:
            return render(request, "clientes/editar_cliente.html", {"error": str(e)})