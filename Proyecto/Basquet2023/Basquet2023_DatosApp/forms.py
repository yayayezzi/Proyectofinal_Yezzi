from django import forms
from Basquet2023_DatosApp.models import Cuenta, equipo

class RegistroCuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['nombre', 'apellido', 'telefono', 'email', 'tipo_cuenta']


class equipoForm(forms.ModelForm):
    class Meta:
        model = equipo
        fields = ['nombre', 'ciudad']