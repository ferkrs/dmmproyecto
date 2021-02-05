
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse
from .models import *
from inicio.models import *
from inicio.forms import *
from .forms import CursoForm
from django.contrib import messages
from datetime import datetime
import django_excel as excel

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