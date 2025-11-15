from django.db import models

# Create your models here.

# ---------- CLIENTE ----------
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


# ---------- VEHÍCULO ----------
class Vehiculo(models.Model):
    PATENTE_CHOICES = [
        ('CAMION', 'Camión'),
        ('FURGON', 'Furgón'),
        ('BUS', 'Bus'),
    ]

    tipo = models.CharField(max_length=20, choices=PATENTE_CHOICES)
    patente = models.CharField(max_length=20, unique=True)
    capacidad_kg = models.IntegerField()
    activo = models.BooleanField(default=True)



    def __str__(self):
        return f"{self.tipo} - {self.patente}"


# ---------- AERONAVE ----------
class Aeronave(models.Model):
    MATRICULA_CHOICES = [
        ('AVION', 'Avión'),
        ('HELICOPTERO', 'Helicóptero'),
    ]

    tipo = models.CharField(max_length=20, choices=MATRICULA_CHOICES)
    matricula = models.CharField(max_length=20, unique=True)
    capacidad_kg = models.IntegerField()
    activo = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.tipo} - {self.matricula}"


# ---------- CONDUCTOR ----------
class Conductor(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    licencia = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)


    def __str__(self):
        return self.nombre


# ---------- PILOTO ----------
class Piloto(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    certificacion = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)


    def __str__(self):
        return self.nombre


# ---------- RUTA ----------
class Ruta(models.Model):
    TIPO_CHOICES = [
        ('TERRESTRE', 'Terrestre'),
        ('AEREA', 'Aérea'),
    ]

    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    tipo_transporte = models.CharField(max_length=20, choices=TIPO_CHOICES)
    distancia_km = models.IntegerField(default=0)



    def __str__(self):
        return f"{self.origen} → {self.destino}"


# ---------- CARGA ----------
class Carga(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    peso_kg = models.FloatField()
    valor = models.IntegerField()

    def __str__(self):
        return f"Carga de {self.cliente} ({self.peso_kg} kg)"


# ---------- DESPACHO ----------
class Despacho(models.Model):
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_RUTA', 'En Ruta'),
        ('ENTREGADO', 'Entregado'),
    ]

    vehiculo = models.ForeignKey(Vehiculo, null=True, blank=True, on_delete=models.SET_NULL)
    aeronave = models.ForeignKey(Aeronave, null=True, blank=True, on_delete=models.SET_NULL)
    conductor = models.ForeignKey(Conductor, null=True, blank=True, on_delete=models.SET_NULL)
    piloto = models.ForeignKey(Piloto, null=True, blank=True, on_delete=models.SET_NULL)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    carga = models.ForeignKey(Carga, on_delete=models.CASCADE)

    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')

    def __str__(self):
        return f"Despacho - {self.estado}"
