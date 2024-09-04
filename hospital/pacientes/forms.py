from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'texto'}),
            'apellidos': forms.TextInput(attrs={'class': 'texto'}),
            'direccion': forms.TextInput(attrs={'class': 'sin-ce'}),
            'area_de_salud': forms.TextInput(attrs={'class': 'sin-ce'})
        }