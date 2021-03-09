
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse
from .models import *
from inicio.models import *
from django.http import JsonResponse
from django.template.loader import render_to_string
from inicio.forms import *
from .forms import CursoForm, CursoModalForm
from django.contrib import messages
from datetime import datetime
from django.urls import reverse_lazy
import django_excel as excel
from django.core.paginator import Paginator
from bootstrap_modal_forms.generic import (
    BSModalDeleteView,
    BSModalUpdateView
)

def servicio_list(request):
    servicios = Curso.objects.all()
    paginator = Paginator(servicios,10)
    page_number=request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'servicios/servicios_list.html', {'servicios': servicios, 'form': CursoForm, 'servicios':page_obj})

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

# Actualizar Servicio
class ServicioUpdateView(BSModalUpdateView):
    model = Curso
    template_name = 'servicios/servicio_edit.html'
    form_class = CursoModalForm
    success_message = 'El servicio fue editado correctamente.'
    success_url = reverse_lazy('servicio_list')

# Actualizacion de integrantes grupo
def integrantes_servicio_async(request, id):
    data = dict()
    if request.method == 'GET':
        integrantes = Curso.objects.get(pk=id).integrantes.all()
        data['table'] = render_to_string(
            '_integrantes-table.html',
            {'integrantes': integrantes},
            request=request
        )
        return JsonResponse(data)

def servicio_integrantes(request, id):
    if request.method == "POST":
        try:
            # Form Persona
            formPersona = PersonaForm(request.POST)
            # Validar si ya existe persona con mismo dpi
            if Persona.objects.filter(cui=formPersona['cui'].value()).count() > 0:
                messages.success(request, "Ya existe este una persona con este DPI, intente otra vez.")
                return redirect('/servicios/integrantes/'+str(id))
            if formPersona.is_valid():
                persona_creada = formPersona.save()
                Curso.objects.get(pk=id).integrantes.add(persona_creada)
                return redirect('/servicios/integrantes/'+str(id))
        except Exception as e:
            print(e)
            return redirect('/servicios/integrantes/'+str(id))
    else:
        # Personas existentes
        personas = Persona.objects.exclude(persona_servicio__id=id)
        formPersona = PersonaForm
        # Info Comunidad
        servicio = Curso.objects.get(pk=id)
        # Integrantes
        integrantes = Curso.objects.get(pk=id).integrantes.all()
        return render(request,'servicios/servicio_integrantes.html', {'integrantes': integrantes, 'servicio': servicio, 'formPersona': formPersona, 'personas': personas})

def servicio_existente(request, id):
    if request.method == "POST":
        try:
            # Form Persona
            persona = Persona.objects.get(pk=request.POST['persona'])
            Curso.objects.get(pk=id).integrantes.add(persona)
            return redirect('/servicios/integrantes/'+str(id))
        except Exception as e:
            print(e)
            return redirect('/servicios/integrantes/'+str(id))

def eliminar_integrante(request, id, servicio):
    # Obtener persona según ID
    persona = Persona.objects.get(pk=id)
    # Obtener fase
    Curso.objects.get(pk=servicio).integrantes.remove(persona)
    return redirect('/servicios/integrantes/'+str(servicio))

def ServicioDelete(request, id):
    servicio = Curso.objects.get(id=id)
    try:
        servicio.delete()
    except:
        pass
    return redirect('servicio_list')


""" REPORTES EXCEL """
def integrantes_servicio_excel(request, id):
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
        'Dirección'
    ])
    # Obtener registros del modelo
    servicio = Curso.objects.get(pk=id)
    integrantes = Curso.objects.get(pk=id).integrantes.all()
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
            persona.direccion
        ])
        count = count + 1
    today = datetime.now()
    strToday = today.strftime("%Y%m%d")

    # Transformar el array a un arreglo
    sheet = excel.pe.Sheet(export)

    return excel.make_response(sheet, "xlsx", file_name="integrantes-"+servicio.get_modalidad_display()+"-"+servicio.nombre+"-"+strToday+".xlsx")