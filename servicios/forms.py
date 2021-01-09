from .models import Curso
from django import forms
from django.forms.fields import DateField
class DateInput(forms.DateInput): 
    input_type = 'date'
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
            'modalidad',
            'nombre',
            'fecha_inicio',
            'fecha_finalizacion',
            'hora_inicio',
            'hora_final',
            'de', 
            'a',
            'integrantes',

            ]
        labels = {
            'modalidad':'Modalidad',
            'nombre': 'Nombre',
            'fecha_inicio':'Fecha de Inicio',
            'fecha_finalizacion':'Fecha de Finalizacion',
            'hora_inicio':'Hora de inicio',
            'hora_final':'Hora final',
            'de':'De', 
            'a':'a',
            'integrantes':'Integrantes',

        }

        widgets = {
            'modalidad' :forms.Select(attrs={'class': 'form-control'}),
            'nombre' :forms.TextInput(attrs={'class': 'form-control '}), 
            'fecha_inicio' :forms.DateInput(),
            'fecha_finalizacion' :forms.DateInput(format='%d/%m/%Y'),
            'hora_inicio' :forms.TimeInput(attrs={'class': 'form-control'}),
            'hora_final' :forms.TimeInput(attrs={'class': 'form-control'}),
            'de' :forms.Select(attrs={'class': 'form-control'}),
            'a' :forms.Select(attrs={'class': 'form-control'}),  
        }
