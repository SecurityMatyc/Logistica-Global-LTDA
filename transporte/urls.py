from rest_framework import routers
from django.urls import path, include
from . import views
from .views import (
    ClienteViewSet, VehiculoViewSet, AeronaveViewSet,
    ConductorViewSet, PilotoViewSet, RutaViewSet,
    CargaViewSet, DespachoViewSet
)

router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'vehiculos', VehiculoViewSet)
router.register(r'aeronaves', AeronaveViewSet)
router.register(r'conductores', ConductorViewSet)
router.register(r'pilotos', PilotoViewSet)
router.register(r'rutas', RutaViewSet)
router.register(r'cargas', CargaViewSet)
router.register(r'despachos', DespachoViewSet)

urlpatterns = [
    # RUTAS API
    path('api/', include(router.urls)),

    # CRUD TEMPLATE
    path('vehiculos/', views.vehiculos_list, name='vehiculos_list'),
    path('vehiculos/agregar/', views.vehiculo_create, name='vehiculo_create'),
    path('vehiculos/editar/<int:id>/', views.vehiculo_edit, name='vehiculo_edit'),
    path('vehiculos/eliminar/<int:id>/', views.vehiculo_delete, name='vehiculo_delete'),
    # AERONAVES
    path('aeronaves/', views.aeronaves_list, name='aeronaves_list'),
    path('aeronaves/agregar/', views.aeronave_create, name='aeronave_create'),
    path('aeronaves/editar/<int:id>/', views.aeronave_edit, name='aeronave_edit'),
    path('aeronaves/eliminar/<int:id>/', views.aeronave_delete, name='aeronave_delete'),
    #conductores
    path('conductores/', views.conductores_list, name='conductores_list'),
    path('conductores/agregar/', views.conductor_create, name='conductor_create'),
    path('conductores/editar/<int:id>/', views.conductor_edit, name='conductor_edit'),
    path('conductores/eliminar/<int:id>/', views.conductor_delete, name='conductor_delete'),
    #pilotos
    path('pilotos/', views.pilotos_list, name='pilotos_list'),
    path('pilotos/agregar/', views.piloto_create, name='piloto_create'),
    path('pilotos/editar/<int:id>/', views.piloto_edit, name='piloto_edit'),
    path('pilotos/eliminar/<int:id>/', views.piloto_delete, name='piloto_delete'),
    #rutas
    path('rutas/', views.rutas_list, name='rutas_list'),
    path('rutas/agregar/', views.ruta_create, name='ruta_create'),
    path('rutas/editar/<int:id>/', views.ruta_edit, name='ruta_edit'),
    path('rutas/eliminar/<int:id>/', views.ruta_delete, name='ruta_delete'),
    # -------- CLIENTES --------
    path("clientes/", views.clientes_list, name="clientes_list"),
    path("clientes/agregar/", views.cliente_create, name="cliente_create"),
    path("clientes/editar/<int:id>/", views.cliente_edit, name="cliente_edit"),
    path("clientes/eliminar/<int:id>/", views.cliente_delete, name="cliente_delete"),
    # -------- CARGAS --------
    path("cargas/", views.cargas_list, name="cargas_list"),
    path("cargas/agregar/", views.carga_create, name="carga_create"),
    path("cargas/editar/<int:id>/", views.carga_edit, name="carga_edit"),
    path("cargas/eliminar/<int:id>/", views.carga_delete, name="carga_delete"),
    # --- DESPACHOS ---
    path('despachos/', views.despachos_list, name='despachos_list'),
    path('despachos/agregar/', views.despacho_create, name='despacho_create'),
    path('despachos/editar/<int:id>/', views.despacho_edit, name='despacho_edit'),
    path('despachos/eliminar/<int:id>/', views.despacho_delete, name='despacho_delete'),



]