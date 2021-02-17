from django.shortcuts import render
from .models import *
from django.views import generic
from .forms import *
from django.core.paginator import Paginator
from inicio.forms import PersonaForm
from django.shortcuts import render, redirect
from bootstrap_modal_forms.generic import (
    BSModalDeleteView,
    BSModalUpdateView
)
from django.urls import reverse_lazy
from django.contrib import messages
from datetime import datetime
# EXCEL
import django_excel as excel

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

def eliminar_comunidad(request, id):
    comunidad = Comunidad.objects.get(id=id)
    try:
        comunidad.delete()
    except:
        pass
    return redirect('alfabetizacion_list')

def comunidades_list(request):
    comunidades = Comunidad.objects.all()
    formComunidad = ComunidadForm
    return render(request, 'alfabetizacion/comunidades_list.html', {'comunidades': comunidades, 'formComunidad': formComunidad})

# Listado de Fases de comunidad
def comunidad_fases_list(request, id):
    formFase = FaseForm
    comunidad = Comunidad.objects.get(pk=id)
    fases = MujeresAlfa.objects.filter(comunidad__id=id, finalizado=False)
    finalizadas = MujeresAlfa.objects.filter(comunidad__id=id, finalizado=True)
    paginator = Paginator(comunidad, 1)
    return render(request, 'alfabetizacion/comunidad_fases.html', {'fases': fases, 'finalizadas': finalizadas, 'comunidad': comunidad, 'formFase': formFase})

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

# Finalizar fase
def fase_finalizar(request, id, aprobados):
    # Obtener la fase para actualizar
    try:
        fase = MujeresAlfa.objects.get(id=id)
        fase.finalizado = True
        fase.aprobados = aprobados
        fase.save()
        messages.success(request,"Fase finalizada correctamente")
        return redirect('/alfabetizacion/fases/1')
    except:
        pass
        return redirect('/alfabetizacion/fases/1')

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
        paginator = Paginator(integrantes, 1)
        return render(request,'alfabetizacion/integrantes_fase.html', {'integrantes': integrantes, 'fase': fase, 'formPersona': formPersona, 'personas': personas})

def existente_fase(request, id):
    if request.method == "POST":
        try:
            # Obtener persona
            persona = Persona.objects.get(pk=request.POST['persona'])
            MujeresAlfa.objects.get(pk=id).integrantes.add(persona)
            messages.success(request,"Integrante agregado correctamente")
            return redirect('/alfabetizacion/fases/'+str(id)+'/integrantes')
        except Exception as e:
            print(e)
            return redirect('/alfabetizacion/fases/'+str(id)+'/integrantes')

def eliminar_integrante(request, id, grupo):
    # Obtener persona según ID
    persona = Persona.objects.get(pk=id)
    # Obtener fase
    MujeresAlfa.objects.get(pk=grupo).integrantes.remove(persona)
    return redirect('/alfabetizacion/fases/'+str(grupo)+'/integrantes')

def eliminar_comunidad(request, id):
    # Obtener persona según ID
    comunidad = Comunidad.objects.get(id=id)
    try:
        comunidad.delete()
    except:
        pass
    return redirect('alfabetizacion_list')
"""
    GENERACION A EXCEL
"""
def fases_excel(request, id):
    export = []
    # Encabezados de excel
    export.append([
        'No.',
        'Alfabetizadora',
        'Ciclo',
        'Integrantes',
        'Fase'
    ])
    # Obtener registros del modelo
    comunidad = Comunidad.objects.get(pk=id)
    fases = MujeresAlfa.objects.filter(comunidad__id=id)
    count = 1
    for fase in fases:
        export.append([
            count,
            fase.nombre_alfabetizadora,
            str(fase.ciclo),
            fase.integrantes.count(),
            fase.get_fase_display(),
        ])
        count = count + 1
    today = datetime.now()
    strToday = today.strftime("%Y%m%d")

    # Transformar el array a un arreglo
    sheet = excel.pe.Sheet(export)

    return excel.make_response(sheet, "xlsx", file_name="fases-"+comunidad.comunidad+"-"+strToday+".xlsx")

def integrantes_fase_excel(request, id):
    export = []
    # Encabezados de excel
    export.append([
        'No.',
        'CUI',
        'Sexo',
        'Primer Nombre',
        'Segundo Nombre',
        'Tercer Nombre',
        'Primer Apellido',
        'Segundo Apellido',
        'Apellido Casada',
        'Fecha Nacimiento',
        'Telefono'
    ])
    # Obtener registros del modelo
    fase = MujeresAlfa.objects.get(pk=id)
    integrantes = MujeresAlfa.objects.get(pk=id).integrantes.all()
    count = 0
    for persona in integrantes:
        export.append([
            count,
            persona.cui,
            persona.get_sexo_display(),
            persona.primer_nombre,
            persona.segundo_nombre,
            persona.tercer_nombre,
            persona.primer_apellido,
            persona.segundo_apellido,
            persona.apellido_casada,
            str(persona.fecha_nacimiento),
            persona.telefono,
        ])
        count = count + 1
    today = datetime.now()
    strToday = today.strftime("%Y%m%d")

    # Transformar el array a un arreglo
    sheet = excel.pe.Sheet(export)

    return excel.make_response(sheet, "xlsx", file_name="integrantes-"+fase.nombre_alfabetizadora+"-"+strToday+".xlsx")