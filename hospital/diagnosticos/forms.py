from django import forms
from .models import Diagnostico

class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = '__all__'
        widgets = {
            'enfermedad': forms.TextInput(attrs={'class': 'sin-ce'}),
            'sintomas': forms.TextInput(attrs={'class': 'sin-ce'})
        }

