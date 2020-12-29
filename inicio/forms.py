from .models import Grupo
from django import forms


class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = [
            'departamento',
            'municipio',
            'identificador',
            'zona',
            'caserio',
            'canton',
            'sector', 
            'aldeas',
            'paraje',
            'nombre_grupo',
            'integrantes',
            ]
        labels = {
            'departamento':'Departamento',
            'municipio': 'Municipio',
            'identificador':'Lugar',
            'zona':'Zona',
            'caserio':'Caserio',
            'canton':'Cantón',
            'sector':'Sector', 
            'aldeas':'Aledeas',
            'paraje':'Paraje',
            'nombre_grupo':'Nombre del grupo',
            'integrantes':'Integrantes',

        }

        widgets = {
            'departamento' :forms.Select(attrs={'class': 'form-control'}),
            'municipio' :forms.Select(attrs={'class': 'form-control'}),
            'identificador' :forms.Select(attrs={'class': 'form-control'}),
            'zona' :forms.Select(attrs={'class': 'form-control'}),
            'caserio' :forms.Select(attrs={'class': 'form-control'}),
            'sector' :forms.Select(attrs={'class': 'form-control'}),
            'canton' :forms.Select(attrs={'class': 'form-control'}),
            'aldeas' :forms.Select(attrs={'class': 'form-control'}),
            'paraje': forms.TextInput(attrs={'class': 'form-control '}),   
            'nombre_grupo': forms.TextInput(attrs={'class': 'form-control '}),                  
           
        }
