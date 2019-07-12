from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import Estacionamiento

class EstacionamientoForm(forms.ModelForm):

    class Meta:
        model = Estacionamiento
        fields = (
            'dueno',
            'tipo',
            'precio_hora',
            'direccion',
            'numero',
            'letra',
            'hora_min',
            'hora_max',
            )
class EstacionamientoeForm(forms.ModelForm):

    class Meta:
        model = Estacionamiento
        fields = (
            )

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'username', 
            'email',
            'rut',
            'nombre_completo',
            'numero_tarjeta',
            'mes_año',
            'tipo',
            )

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = (
            'username', 
            'email',
            'rut',
            'nombre_completo',
            'numero_tarjeta',
            'mes_año',
            )