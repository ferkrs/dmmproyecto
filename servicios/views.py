from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse
from .models import *  
from .forms import CursoForm
from django.contrib import messages

class CursoList(generic.ListView):
    queryset = Curso.objects.all()
    template_name = 'servicios/servicios_list.html'

def servicio_crear(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            try: 
                form.save()
                messages.success(request,"Se ha creado el servicio")
                return render(request, 'servicios/servicios_add.html', {'servicio': servicios})
            except:  
                pass
                return redirect('servicio_list') 
    else:
        form = CursoForm()
    return render(request, 'servicios/servicios_add.html', {'form': form})

def ServicioDelete(request, id):
    servicio = Curso.objects.get(id=id)
    try:
        servicio.delete()
    except: 
        pass
    return redirect('servicio_list')  
    