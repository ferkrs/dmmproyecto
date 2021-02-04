from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse
from .models import *  
from .forms import *
from django.contrib import messages

def reporte_grupo(request):
    if request.method == 'POST':
        reporteg = ReporteGruposForm(request.POST)
        if reporteg.is_valid():
            try: 
                reporteg.save()
                messages.success(request,"Se ha creado el reporte de grupos correctamente")
                return render(request, 'reportes/grupos/create_reporte_grupos.html', {'reporteg': reporteg})
            except:  
                pass
                return redirect('reporte_grupo') 
    else:
        reporteg = ReporteGruposForm()
    return render(request,'reportes/grupos/create_reporte_grupos.html', {'reporteg': reporteg})



def reporte_servicio(request):
    if request.method == 'POST':
        reportes = ReporteserviciosForm(request.POST)
        if reportes.is_valid():
            try: 
                reportes.save()
                messages.success(request,"Se ha creado el reporte de servicios correctamente")
                return render(request, 'reportes/servicios/create_reporte_servicios.html', {'reportes': reportes})
            except:  
                pass
                return redirect('reporte_servicio') 
    else:
        reportes = ReporteserviciosForm()
    return render(request,'reportes/servicios/create_reporte_servicios.html', {'reportes': reportes})
