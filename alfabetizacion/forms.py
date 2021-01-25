from .models import Comunidad, MujeresAlfa
from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm

class ComunidadForm(forms.ModelForm):
    class Meta:
        model = Comunidad
        fields = [
            'comunidad',
        ]
        labels = {
            'comunidad': 'Comunidad',
        }
        widgets = {
            'comunidad': forms.TextInput(attrs={'class': 'form-control ', 'required': True}),
        }

class ComunidadModalForm(BSModalModelForm):
    class Meta:
        model = Comunidad
        fields = [
            'comunidad',
        ]
        labels = {
            'comunidad': 'Comunidad',
        }
        widgets = {
            'comunidad': forms.TextInput(attrs={'class': 'form-control ', 'required': True}),
        }

class FaseForm(forms.ModelForm):
    class Meta:
        model = MujeresAlfa
        fields = [
            'nombre_alfabetizadora',
            'ciclo',
            'fase'
        ]
        labels = {
            'nombre_alfabetizadora': 'Alfabetizadora',
            'ciclo': 'Ciclo',
            'fase': 'Fase'
        }
        widgets = {
            'nombre_alfabetizadora': forms.TextInput(attrs={'class': 'form-control ', 'required': True}),
            'ciclo': forms.DateInput(attrs={'class':'form-control', 'type':'date', 'required': True}),
            'fase': forms.Select(attrs={'class': 'form-control', 'required': True}),
        }

class FaseModalForm(BSModalModelForm):
    class Meta:
        model = MujeresAlfa
        fields = [
            'nombre_alfabetizadora',
            'ciclo',
            'fase'
        ]
        labels = {
            'nombre_alfabetizadora': 'Alfabetizadora',
            'ciclo': 'Ciclo',
            'fase': 'Fase'
        }
        widgets = {
            'nombre_alfabetizadora': forms.TextInput(attrs={'class': 'form-control ', 'required': True}),
            'ciclo': forms.DateInput(attrs={'class':'form-control', 'type':'date', 'required': True}),
            'fase': forms.Select(attrs={'class': 'form-control', 'required': True}),
        }