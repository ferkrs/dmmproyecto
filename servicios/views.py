from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse
from .models import *
from inicio.models import *
from inicio.forms import *
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
    else:
        form = CursoForm()
    return render(request, 'servicios/servicios_add.html', {'form': form})

def servicio_integrantes(request, id):
    if request.method == "POST":
        try:
            # Form Persona
            formPersona = PersonaForm(request.POST)
            if formPersona.is_valid():
                persona_creada = formPersona.save()
                Curso.objects.get(pk=id).integrantes.add(persona_creada)
                return redirect('/servicios/integrantes/'+str(id))
        except Exception as e:
            print(e)
            return redirect('/servicios/integrantes/'+str(id))
    else:
        # Personas existentes
        formPersona = PersonaForm
        # Info Comunidad
        servicio = Curso.objects.get(pk=id)
        # Integrantes
        integrantes = Curso.objects.get(pk=id).integrantes.all()
        return render(request,'servicios/servicio_integrantes.html', {'integrantes': integrantes, 'servicio': servicio, 'formPersona': formPersona})

def eliminar_integrante(request, id, servicio):
    # Obtener persona según ID
    persona = Persona.objects.get(pk=id)
    # Obtener fase
    Curso.objects.get(pk=servicio).integrantes.remove(persona)
    return redirect('/servicios/integrantes/'+str(servicio))