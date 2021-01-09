from .models import Grupo
from django import forms


class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = [
            'nombre_grupo',
            'departamento',
            'municipio',
            'identificador',
            'zona',
            'caserio',
            'canton',
            'sector', 
            'aldeas',
            'paraje',

            ]
        labels = {
            'nombre_grupo':'Nombre del grupo',
            'departamento':'Departamento',
            'municipio': 'Municipio',
            'identificador':'Lugar',
            'zona':'Zona',
            'caserio':'Caserio',
            'canton':'Cantón',
            'sector':'Sector', 
            'aldeas':'Aledeas',
            'paraje':'Paraje',


        }

        widgets = {
            'nombre_grupo': forms.TextInput(attrs={'class': 'form-control '}),  
            'departamento' :forms.Select(attrs={'class': 'form-control'}),
            'municipio' :forms.Select(attrs={'class': 'form-control'}),
            'identificador' :forms.Select(attrs={'class': 'form-control'}),
            'zona' :forms.Select(attrs={'class': 'form-control'}),
            'caserio' :forms.Select(attrs={'class': 'form-control'}),
            'sector' :forms.Select(attrs={'class': 'form-control'}),
            'canton' :forms.Select(attrs={'class': 'form-control'}),
            'aldeas' :forms.Select(attrs={'class': 'form-control'}),
            'paraje': forms.TextInput(attrs={'class': 'form-control '}),   
           
        }
