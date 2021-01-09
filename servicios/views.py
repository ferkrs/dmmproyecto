from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse
from .models import *  
from .forms import CursoForm

class CursoList(generic.ListView):
    queryset = Curso.objects.all()
    template_name = 'servicios/servicios_list.html'


def servicio_crear(request):
    servicio = CursoForm(request)
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form = form.save()
            return render(request, 'servicios/servicios_add.html', {'servicio': servicios})
    else:
        form = CursoForm()
    return render(request, 'servicios/servicios_add.html', {'form': form})