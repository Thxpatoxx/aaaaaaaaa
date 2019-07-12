from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    rut = models.CharField(max_length=20)
    nombre_completo = models.CharField(max_length=80)
    numero_tarjeta = models.CharField(max_length=16)
    mes_año = models.CharField(max_length=20)
    TIPO = (
        ('ARRENDATARIO','ARRENDATARIO'),
        ('COMUN','COMUN'),
    )
    tipo = models.CharField(max_length=80,choices=TIPO,default='COMUN')
    
    def __str__(self):
        return self.rut

class Estacionamiento(models.Model):
    dueno = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    ESTADO = (
        ('DISPONIBLE','DISPONIBLE'),
        ('NO DISPONIBLE','NO DISPONIBLE'),
    )
    estado = models.CharField(max_length=80,choices=ESTADO,default='DISPONIBLE')
    TIPO = (
        ('PUBLICO','PUBLICO'),
        ('PRIVADO','PRIVADO'),
    )
    tipo = models.CharField(max_length=80,choices=TIPO,default='PRIVADO')
    precio_hora = models.CharField(max_length=4)
    direccion = models.CharField(max_length=30)
    numero = models.CharField(max_length=3)
    letra = models.CharField(max_length=2)
    planta = models.CharField(max_length=2)
    hora_min = models.CharField(max_length=5)
    hora_max = models.CharField(max_length=5)
    def __str__(self):
        return self.estado