from django import forms
from .models import (
    Vehiculo, Aeronave, Conductor, Piloto,
    Ruta, Carga, Despacho, Cliente
)

# ===========================
# FORMULARIO VEHÍCULO
# ===========================
class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['tipo', 'patente', 'capacidad_kg', 'activo']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'patente': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad_kg': forms.NumberInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


# ===========================
# FORMULARIO AERONAVE
# ===========================
class AeronaveForm(forms.ModelForm):
    class Meta:
        model = Aeronave
        fields = ['tipo', 'matricula', 'capacidad_kg', 'activo']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad_kg': forms.NumberInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


# ===========================
# FORMULARIO CONDUCTOR
# ===========================
class ConductorForm(forms.ModelForm):
    class Meta:
        model = Conductor
        fields = ['nombre','rut','licencia', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'licencia': forms.TextInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


# ===========================
# FORMULARIO PILOTO
# ===========================
class PilotoForm(forms.ModelForm):
    class Meta:
        model = Piloto
        fields = ['nombre','rut', 'certificacion', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'certificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


# ===========================
# FORMULARIO RUTA
# ===========================
class RutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = ['origen', 'destino', 'tipo_transporte', 'distancia_km']
        widgets = {
            'origen': forms.TextInput(attrs={'class': 'form-control'}),
            'destino': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_transporte': forms.Select(attrs={'class': 'form-select'}),
            'distancia_km': forms.NumberInput(attrs={'class': 'form-control'}),
        }


# ===========================
# FORMULARIO CARGA
# ===========================
class CargaForm(forms.ModelForm):
    class Meta:
        model = Carga
        fields = ['cliente', 'descripcion', 'peso_kg', 'valor']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'peso_kg': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
        }


# ===========================
# FORMULARIO DESPACHO
# ===========================
class DespachoForm(forms.ModelForm):
    class Meta:
        model = Despacho
        fields = [
            'vehiculo', 'aeronave', 'conductor', 'piloto',
            'ruta', 'carga', 'estado'
        ]
        widgets = {
            'vehiculo': forms.Select(attrs={'class': 'form-select'}),
            'aeronave': forms.Select(attrs={'class': 'form-select'}),
            'conductor': forms.Select(attrs={'class': 'form-select'}),
            'piloto': forms.Select(attrs={'class': 'form-select'}),
            'ruta': forms.Select(attrs={'class': 'form-select'}),
            'carga': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }
