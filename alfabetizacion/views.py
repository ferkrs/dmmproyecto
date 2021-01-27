from django.shortcuts import render
from .models import *
from django.views import generic
from .forms import *
from inicio.forms import PersonaForm
from django.shortcuts import render, redirect
from bootstrap_modal_forms.generic import (
    BSModalDeleteView,
    BSModalUpdateView
)
from django.urls import reverse_lazy
from django.contrib import messages

# Lista Comunidades
def comunidad_create(request):
    if request.method == 'POST':
        try:
            formComunidad = ComunidadForm(request.POST)
            if formComunidad.is_valid():
                formComunidad.save()
                return redirect('/alfabetizacion/list')
        except Exception as e:
            print(e)
            return redirect('/alfabetizacion/list')

# Edicion de comunidad
class ComunidadUpdateView(BSModalUpdateView):
    model = Comunidad
    template_name = 'alfabetizacion/comunidad_edit.html'
    form_class = ComunidadModalForm
    success_message = 'La información fue editada correctamente.'
    success_url = reverse_lazy('alfabetizacion_list')

def comunidades_list(request):
    comunidades = Comunidad.objects.all()
    formComunidad = ComunidadForm 
    return render(request, 'alfabetizacion/comunidades_list.html', {'comunidades': comunidades, 'formComunidad': formComunidad})

# Listado de Fases de comunidad
def comunidad_fases_list(request, id):
    formFase = FaseForm
    comunidad = Comunidad.objects.get(pk=id)
    fases = MujeresAlfa.objects.filter(comunidad__id=id)
    return render(request, 'alfabetizacion/comunidad_fases.html', {'fases': fases, 'comunidad': comunidad, 'formFase': formFase})

def crear_fase(request, id):
    if request.method == "POST":
        formFase = FaseForm(request.POST)
        if formFase.is_valid():
            # Obtener la comunidad segun id
            comunidad_encontrada = Comunidad.objects.get(pk=id)
            fase = formFase.save(commit=False)
            fase.comunidad = comunidad_encontrada
            fase.save()
            messages.success(request,"Fase agregada correctamente")
    return redirect('/alfabetizacion/fases/'+str(id))

class FaseUpdateView(BSModalUpdateView):
    model = MujeresAlfa
    template_name = 'alfabetizacion/fase_edit.html'
    form_class = FaseModalForm
    success_message = 'La información fue editada correctamente.'
    success_url = reverse_lazy('alfabetizacion_list')

class FaseDeleteView(BSModalDeleteView):
    model = MujeresAlfa
    template_name = 'alfabetizacion/fase_delete.html'
    form_class = FaseModalForm
    success_message = 'La fase fue eliminada correctamente.'
    success_url = reverse_lazy('alfabetizacion_list')

def integrantes_fase(request, id):
    if request.method == "POST":
        try:
            # Form Persona
            formPersona = PersonaForm(request.POST)
            if formPersona.is_valid():
                persona_creada = formPersona.save()
                MujeresAlfa.objects.get(pk=id).integrantes.add(persona_creada)
                return redirect('/alfabetizacion/fases/'+str(id)+'/integrantes')
        except Exception as e:
            print(e)
            return redirect('/alfabetizacion/fases/'+str(id)+'/integrantes')
    else:
        # Personas existentes
        personas = Persona.objects.all()
        formPersona = PersonaForm
        # Info Comunidad
        fase = MujeresAlfa.objects.get(pk=id)
        # Integrantes
        integrantes = MujeresAlfa.objects.get(pk=id).integrantes.all()
        return render(request,'alfabetizacion/integrantes_fase.html', {'integrantes': integrantes, 'fase': fase, 'formPersona': formPersona, 'personas': personas})

def eliminar_integrante(request, id, grupo):
    # Obtener persona según ID
    persona = Persona.objects.get(pk=id)
    # Obtener fase
    MujeresAlfa.objects.get(pk=grupo).integrantes.remove(persona)
    return redirect('/alfabetizacion/fases/'+str(grupo)+'/integrantes')