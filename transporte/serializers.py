from rest_framework import serializers
from .models import (
    Cliente, Vehiculo, Aeronave, Conductor,
    Piloto, Ruta, Carga, Despacho
)


# ---------- CLIENTE ----------
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


# ---------- VEHÍCULO ----------
class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'


# ---------- AERONAVE ----------
class AeronaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aeronave
        fields = '__all__'


# ---------- CONDUCTOR ----------
class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = '__all__'


# ---------- PILOTO ----------
class PilotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piloto
        fields = '__all__'


# ---------- RUTA ----------
class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = '__all__'


# ---------- CARGA ----------
class CargaSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)

    class Meta:
        model = Carga
        fields = '__all__'


# ---------- DESPACHO ----------
class DespachoSerializer(serializers.ModelSerializer):
    vehiculo_patente = serializers.CharField(source='vehiculo.patente', read_only=True)
    aeronave_matricula = serializers.CharField(source='aeronave.matricula', read_only=True)
    ruta_info = serializers.CharField(source='ruta.__str__', read_only=True)
    cliente = serializers.CharField(source='carga.cliente.nombre', read_only=True)

    class Meta:
        model = Despacho
        fields = '__all__'




