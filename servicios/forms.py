from .models import Curso
from django import forms
from django.forms.fields import DateField
class DateInput(forms.DateInput): 
    input_type = 'date', 
    input_type = 'time'
    
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

        }

        widgets = {
            'modalidad' :forms.Select(attrs={'class': 'form-control'}),
            'nombre' :forms.TextInput(attrs={'class': 'form-control '}), 
            'fecha_inicio' :forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'fecha_finalizacion' :forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'hora_inicio' :forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
            'hora_final' :forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
            'de' :forms.Select(attrs={'class': 'form-control'}),
            'a' :forms.Select(attrs={'class': 'form-control'}),  
        }
