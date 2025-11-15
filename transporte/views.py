from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehiculo
from .forms import VehiculoForm
from .models import Aeronave
from .forms import AeronaveForm
from .models import Conductor
from .forms import ConductorForm
from .models import Piloto
from .forms import PilotoForm
from .models import Ruta
from .forms import RutaForm
from .models import Carga
from .forms import CargaForm
from .models import Despacho
from .forms import DespachoForm
from .forms import ClienteForm
from .models import Cliente
from django.db.models import Q



# Create your views here.
from rest_framework import viewsets
from .models import (
    Cliente, Vehiculo, Aeronave, Conductor,
    Piloto, Ruta, Carga, Despacho
)
from .serializers import (
    ClienteSerializer, VehiculoSerializer, AeronaveSerializer,
    ConductorSerializer, PilotoSerializer, RutaSerializer,
    CargaSerializer, DespachoSerializer
)


# ---------- CLIENTE ----------
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


# ---------- VEHÍCULO ----------
class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer


# ---------- AERONAVE ----------
class AeronaveViewSet(viewsets.ModelViewSet):
    queryset = Aeronave.objects.all()
    serializer_class = AeronaveSerializer


# ---------- CONDUCTOR ----------
class ConductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer


# ---------- PILOTO ----------
class PilotoViewSet(viewsets.ModelViewSet):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer


# ---------- RUTA ----------
class RutaViewSet(viewsets.ModelViewSet):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer


# ---------- CARGA ----------
class CargaViewSet(viewsets.ModelViewSet):
    queryset = Carga.objects.all()
    serializer_class = CargaSerializer


# ---------- DESPACHO ----------
class DespachoViewSet(viewsets.ModelViewSet):
    queryset = Despacho.objects.all()
    serializer_class = DespachoSerializer




# LISTAR
def vehiculos_list(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, "vehiculos/list.html", {"vehiculos": vehiculos})

# CREAR
def vehiculo_create(request):
    form = VehiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("vehiculos_list")
    return render(request, "vehiculos/form.html", {"form": form, "titulo": "Agregar Vehículo"})

# EDITAR
def vehiculo_edit(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    form = VehiculoForm(request.POST or None, instance=vehiculo)
    if form.is_valid():
        form.save()
        return redirect("vehiculos_list")
    return render(request, "vehiculos/form.html", {"form": form, "titulo": "Editar Vehículo"})

# ELIMINAR
def vehiculo_delete(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    if request.method == "POST":
        vehiculo.delete()
        return redirect("vehiculos_list")
    return render(request, "vehiculos/delete.html", {"vehiculo": vehiculo})


# AERONAVE CRUD VIEWS

# ========== LISTAR ==========
def aeronaves_list(request):
    aeronaves = Aeronave.objects.all()
    return render(request, "aeronave/list.html", {"aeronaves": aeronaves})


# ========== CREAR ==========
def aeronave_create(request):
    if request.method == "POST":
        form = AeronaveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("aeronaves_list")
    else:
        form = AeronaveForm()

    return render(request, "aeronave/form.html", {"form": form, "titulo": "Agregar Aeronave"})


# ========== EDITAR ==========
def aeronave_edit(request, id):
    aeronave = get_object_or_404(Aeronave, id=id)

    if request.method == "POST":
        form = AeronaveForm(request.POST, instance=aeronave)
        if form.is_valid():
            form.save()
            return redirect("aeronaves_list")
    else:
        form = AeronaveForm(instance=aeronave)

    return render(request, "aeronave/form.html", {"form": form, "titulo": "Editar Aeronave"})


# ========== ELIMINAR ==========
def aeronave_delete(request, id):
    aeronave = get_object_or_404(Aeronave, id=id)

    if request.method == "POST":
        aeronave.delete()
        return redirect("aeronaves_list")

    return render(request, "aeronave/delete.html", {"aeronave": aeronave})


# ========== LISTAR CONDUCTORES ==========
def conductores_list(request):
    """
    Muestra todos los conductores registrados.
    """
    conductores = Conductor.objects.all()
    return render(request, "conductor/list.html", {"conductores": conductores})


# ========== CREAR CONDUCTOR ==========
def conductor_create(request):
    """
    Crea un nuevo conductor usando ConductorForm.
    Si el método es POST, guarda. Si no, muestra el formulario vacío.
    """
    if request.method == "POST":
        form = ConductorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("conductores_list")
    else:
        form = ConductorForm()

    return render(request, "conductor/form.html", {"form": form, "titulo": "Agregar Conductor"})


# ========== EDITAR CONDUCTOR ==========
def conductor_edit(request, id):
    """
    Edita un conductor existente identificado por su ID.
    Si no existe, lanza error 404 automáticamente.
    """
    conductor = get_object_or_404(Conductor, id=id)

    if request.method == "POST":
        form = ConductorForm(request.POST, instance=conductor)
        if form.is_valid():
            form.save()
            return redirect("conductores_list")
    else:
        form = ConductorForm(instance=conductor)

    return render(request, "conductor/form.html", {"form": form, "titulo": "Editar Conductor"})


# ========== ELIMINAR CONDUCTOR ==========
def conductor_delete(request, id):
    """
    Confirma y elimina un conductor.
    Muestra una página de confirmación antes de borrar.
    """
    conductor = get_object_or_404(Conductor, id=id)

    if request.method == "POST":
        conductor.delete()
        return redirect("conductores_list")

    return render(request, "conductor/delete.html", {"conductor": conductor})


# ========== LISTAR PILOTOS ==========
def pilotos_list(request):
    """
    Lista todos los pilotos registrados.
    """
    pilotos = Piloto.objects.all()
    return render(request, "piloto/list.html", {"pilotos": pilotos})


# ========== CREAR PILOTO ==========
def piloto_create(request):
    """
    Crea un nuevo piloto.
    """
    if request.method == "POST":
        form = PilotoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pilotos_list")
    else:
        form = PilotoForm()

    return render(request, "piloto/form.html", {"form": form, "titulo": "Agregar Piloto"})


# ========== EDITAR PILOTO ==========
def piloto_edit(request, id):
    """
    Edita un piloto existente.
    """
    piloto = get_object_or_404(Piloto, id=id)

    if request.method == "POST":
        form = PilotoForm(request.POST, instance=piloto)
        if form.is_valid():
            form.save()
            return redirect("pilotos_list")
    else:
        form = PilotoForm(instance=piloto)

    return render(request, "piloto/form.html", {"form": form, "titulo": "Editar Piloto"})


# ========== ELIMINAR PILOTO ==========
def piloto_delete(request, id):
    """
    Muestra confirmación y elimina un piloto.
    """
    piloto = get_object_or_404(Piloto, id=id)

    if request.method == "POST":
        piloto.delete()
        return redirect("pilotos_list")

    return render(request, "piloto/delete.html", {"piloto": piloto})


# ========== LISTAR RUTAS ==========
def rutas_list(request):
    """
    Lista las rutas con filtros de búsqueda por origen, destino
    y por tipo de transporte.
    """
    rutas = Ruta.objects.all()

    # --- BÚSQUEDA ---
    buscar = request.GET.get("buscar")
    tipo = request.GET.get("tipo")

    if buscar:
        rutas = rutas.filter(
            Q(origen__icontains=buscar) |
            Q(destino__icontains=buscar)
        )

    if tipo:
        rutas = rutas.filter(tipo_transporte=tipo)

    return render(request, "ruta/list.html", {"rutas": rutas})



# ========== CREAR RUTA ==========
def ruta_create(request):
    """
    Crea una nueva ruta.
    """
    if request.method == "POST":
        form = RutaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("rutas_list")
    else:
        form = RutaForm()

    return render(request, "ruta/form.html", {"form": form, "titulo": "Agregar Ruta"})


# ========== EDITAR RUTA ==========
def ruta_edit(request, id):
    """
    Edita una ruta existente.
    Si no existe, retorna error 404.
    """
    ruta = get_object_or_404(Ruta, id=id)

    if request.method == "POST":
        form = RutaForm(request.POST, instance=ruta)
        if form.is_valid():
            form.save()
            return redirect("rutas_list")
    else:
        form = RutaForm(instance=ruta)

    return render(request, "ruta/form.html", {"form": form, "titulo": "Editar Ruta"})


# ========== ELIMINAR RUTA ==========
def ruta_delete(request, id):
    """
    Muestra confirmación y luego elimina la ruta seleccionada.
    """
    ruta = get_object_or_404(Ruta, id=id)

    if request.method == "POST":
        ruta.delete()
        return redirect("rutas_list")

    return render(request, "ruta/delete.html", {"ruta": ruta})

# ---------- LISTAR CLIENTES ----------
def clientes_list(request):
    clientes = Cliente.objects.all()
    return render(request, "cliente/list.html", {"clientes": clientes})

# ---------- CREAR CLIENTE ----------
def cliente_create(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clientes_list")
    else:
        form = ClienteForm()

    return render(request, "cliente/form.html", {"form": form, "titulo": "Agregar Cliente"})

# ---------- EDITAR CLIENTE ----------
def cliente_edit(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("clientes_list")
    else:
        form = ClienteForm(instance=cliente)

    return render(request, "cliente/form.html", {"form": form, "titulo": "Editar Cliente"})

# ---------- ELIMINAR CLIENTE ----------
def cliente_delete(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "POST":
        cliente.delete()
        return redirect("clientes_list")

    return render(request, "cliente/delete.html", {"cliente": cliente})


# ---------- LISTAR CARGAS ----------
def cargas_list(request):
    cargas = Carga.objects.select_related("cliente").all()
    clientes = Cliente.objects.all()

    buscar = request.GET.get("buscar")
    cliente_id = request.GET.get("cliente")

    # --- FILTRO POR BÚSQUEDA ---
    if buscar:
        cargas = cargas.filter(descripcion__icontains=buscar)

    # --- FILTRO POR CLIENTE ---
    if cliente_id:
        cargas = cargas.filter(cliente__id=cliente_id)

    return render(request, "carga/list.html", {
        "cargas": cargas,
        "clientes": clientes
    })

# ---------- CREAR CARGA ----------
def carga_create(request):
    if request.method == "POST":
        form = CargaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cargas_list")
    else:
        form = CargaForm()

    return render(request, "carga/form.html", {"form": form, "titulo": "Agregar Carga"})


# ---------- EDITAR CARGA ----------
def carga_edit(request, id):
    carga = get_object_or_404(Carga, id=id)

    if request.method == "POST":
        form = CargaForm(request.POST, instance=carga)
        if form.is_valid():
            form.save()
            return redirect("cargas_list")
    else:
        form = CargaForm(instance=carga)

    return render(request, "carga/form.html", {"form": form, "titulo": "Editar Carga"})


# ---------- ELIMINAR CARGA ----------
def carga_delete(request, id):
    carga = get_object_or_404(Carga, id=id)

    if request.method == "POST":
        carga.delete()
        return redirect("cargas_list")

    return render(request, "carga/delete.html", {"carga": carga})

# ========== LISTAR DESPACHOS ==========
def despachos_list(request):
    """
    Muestra todos los despachos registrados.
    """
    despachos = Despacho.objects.all().order_by("-id")
    return render(request, "despacho/list.html", {"despachos": despachos})


# ========== CREAR DESPACHO ==========
def despacho_create(request):
    """
    Crea un nuevo despacho seleccionando vehículo/aeronave, ruta y carga.
    """
    if request.method == "POST":
        form = DespachoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("despachos_list")
    else:
        form = DespachoForm()

    return render(request, "despacho/form.html", {"form": form, "titulo": "Crear Despacho"})


# ========== EDITAR DESPACHO ==========
def despacho_edit(request, id):
    """
    Edita un despacho existente. Error 404 si no existe.
    """
    despacho = get_object_or_404(Despacho, id=id)

    if request.method == "POST":
        form = DespachoForm(request.POST, instance=despacho)
        if form.is_valid():
            form.save()
            return redirect("despachos_list")
    else:
        form = DespachoForm(instance=despacho)

    return render(request, "despacho/form.html", {"form": form, "titulo": "Editar Despacho"})


# ========== ELIMINAR DESPACHO ==========
def despacho_delete(request, id):
    """
    Página de confirmación para eliminar un despacho.
    """
    despacho = get_object_or_404(Despacho, id=id)

    if request.method == "POST":
        despacho.delete()
        return redirect("despachos_list")

    return render(request, "despacho/delete.html", {"despacho": despacho})




