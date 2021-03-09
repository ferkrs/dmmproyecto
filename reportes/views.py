from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.views import generic
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from inicio.models import Grupo
from .forms import *
from django.contrib import messages
from django.db.models import Q, Sum, Count
from django.http import JsonResponse
# Bootstrap Modals
from bootstrap_modal_forms.generic import (
    BSModalDeleteView,
    BSModalUpdateView
)
from datetime import datetime
# EXCEL
import django_excel as excel

# Funcion para verificar si el usuario autenticado es administrador
def administrador_check(user):
    if(user.rol == 0):
        return True
    else:
        return False

def reporte_grupo(request):
    mis_reportes = ReporteGrupos.objects.filter(user=request.user)
    if request.method == 'POST':
        reporteg = ReporteGruposForm(request.POST)
        if reporteg.is_valid():
            try:
                reporte = reporteg.save(commit=False)
                reporte.user = request.user
                reporte.save()
                messages.success(request,"Se ha creado el reporte de grupos correctamente")
                return redirect('reporte_grupo')
            except:
                pass
                return redirect('reporte_grupo')
    else:
        reporteg = ReporteGruposForm()
        # Obtener reportes del usuario
    return render(request,'reportes/grupos/create_reporte_grupos.html', {'reporteg': reporteg, 'mis_reportes': mis_reportes})

# Reporte Update
class ReporteGrupoUpdateView(BSModalUpdateView):
    model = ReporteGrupos
    template_name = 'reportes/grupos/edit_reporte.html'
    form_class = ReporteGruposModal
    success_message = 'El reporte fue editado correctamente.'
    success_url = reverse_lazy('reporte_grupo')

# Reporte Delete
def reporte_grupo_delete(request, id):
    try:
        # Obtener reporte
        reporte = ReporteGrupos.objects.get(id=id)
        reporte.delete()
        return redirect('/reportegrupos/crear')
    except:
        pass
        return redirect('/reportegrupos/crear')

def reporte_servicio(request):
    # Reportes del usuario
    mis_reportes = ReporteServicios.objects.filter(user=request.user)
    if request.method == 'POST':
        reportes = ReporteserviciosForm(request.POST)
        if reportes.is_valid():
            try:
                reporte = reportes.save(commit=False)
                reporte.user = request.user
                reporte.save()
                messages.success(request,"Se ha creado el reporte de servicios correctamente")
                return redirect('reporte_servicio')
            except:
                pass
                return redirect('reporte_servicio')
    else:
        reportes = ReporteserviciosForm()
    return render(request,'reportes/servicios/create_reporte_servicios.html', {'reportes': reportes, 'mis_reportes': mis_reportes})

# Reporte Delete
def reporte_servicio_delete(request, id):
    try:
        # Obtener reporte
        reporte = ReporteServicios.objects.get(id=id)
        reporte.delete()
        return redirect('/reporteservicios/crear')
    except:
        pass
        return redirect('/reporteservicios/crear')

# Reporte Update
class ReporteServicioUpdateView(BSModalUpdateView):
    model = ReporteServicios
    template_name = 'reportes/servicios/edit_reporte.html'
    form_class = ReporteServiciosModal
    success_message = 'El reporte fue editado correctamente.'
    success_url = reverse_lazy('reporte_servicio')

@user_passes_test(administrador_check)
def reporte_grupos_admin(request):
    ejes = Eje.objects.all()
    grupos = Grupo.objects.all()
    users = Usuario.objects.all()
    identificadores = [
        {'id': 0, 'tipo': 'AREA RURAL'},
        {'id': 1, 'tipo': 'AREA URBANA'},
        {'id': 2, 'tipo': 'LLANO GRANDE'}
    ]
    aldeas = [
        {"id": 1, "nombre": "CANTEL"}, {"id": 2, "nombre": "CORRAL GRANDE"},
        {"id": 3, "nombre": "CHAMPOLLAP"},{"id": 4, "nombre": "CHIM"},
        {"id": 5, "nombre": "EL CEDRO"},{"id": 6, "nombre": "EL TABLERO"},
        {"id": 7, "nombre": "LA GRANDEZA"},{"id": 8, "nombre": "MÁVIL"},
        {"id": 9, "nombre": "PIEDRA GRANDE"},{"id": 10, "nombre": "PROVINCIA CHIQUITA"},
        {"id": 11, "nombre": "SACUCHÚM"},{"id": 12, "nombre": "SAN ANDRÉS CHÁPIL"},
        {"id": 13, "nombre": "SAN ISIDRO CHAMAC"},{"id": 14, "nombre": "SAN JOSÉ CÁBEN"},
        {"id": 15, "nombre": "SAN PEDRO PETZ"},{"id": 16, "nombre": "SANTA TERESA"},
        {"id": 17, "nombre": "SAN FRANCISCO SOCHE"},
    ]
    # Eje seleccionado
    reportes = []
    queryReportes = Q()
    if request.method == "POST":
        eje_seleccionado = request.POST.get('eje', False)
        grupo_seleccionado = request.POST.get('grupo', False)
        identificador = request.POST.get('identificador', False)
        aldea = request.POST.get('aldea', False)
        responsable = request.POST.get('responsable', False)
        if eje_seleccionado == "0" and grupo_seleccionado == "0" and identificador == "0" and responsable == "0":
            reportes = ReporteGrupos.objects.all()
        else:
            # Si se selecciono Eje
            if eje_seleccionado != "0":
                queryReportes = queryReportes & Q(eje_trabajo = eje_seleccionado)
            # Si se selecciono Grupo
            if grupo_seleccionado != "0":
                queryReportes = queryReportes & Q(grupo = grupo_seleccionado)
            if identificador != "100":
                queryReportes = queryReportes & Q(grupo__identificador=identificador)
            if aldea != "0":
                queryReportes = queryReportes & Q(grupo__aldeas=aldea)
            if responsable != "0":
                queryReportes = queryReportes & Q(user__id=responsable)
            reportes = ReporteGrupos.objects.filter(queryReportes)
        return render(request,'reportes/grupos/admin.html', {'users': users, 'ejes': ejes, 'grupos': grupos, 'identificadores': identificadores, 'aldeas': aldeas, 'reportes': reportes})
    else:
        return render(request,'reportes/grupos/admin.html', {'users': users, 'ejes': ejes, 'grupos': grupos, 'identificadores': identificadores, 'aldeas': aldeas})

@user_passes_test(administrador_check)
def reporte_grupos_admin_excel(request):
    ejes = Eje.objects.all()
    grupos = Grupo.objects.all()
    users = Usuario.objects.all()
    years = [
        {'id': 2020, "texto": "2020"},
        {'id': 2021, "texto": "2021"},
        {'id': 2022, 'texto': "2022"},
        {'id': 2023, 'texto': "2023"},
        {'id': 2024, 'texto': "2024"},
        {'id': 2025, 'texto': "2025"},
        {'id': 2026, 'texto': "2026"},
        {'id': 2027, 'texto': "2027"},
        {'id': 2028, 'texto': "2028"},
        {'id': 2029, 'texto': "2029"},
        {'id': 2030, 'texto': "2030"},
        {'id': 2031, 'texto': "2031"},
    ]
    identificadores = [
        {'id': 0, 'tipo': 'AREA RURAL'},
        {'id': 1, 'tipo': 'AREA URBANA'},
        {'id': 2, 'tipo': 'LLANO GRANDE'}
    ]
    aldeas = [
        {"id": 1, "nombre": "CANTEL"}, {"id": 2, "nombre": "CORRAL GRANDE"},
        {"id": 3, "nombre": "CHAMPOLLAP"},{"id": 4, "nombre": "CHIM"},
        {"id": 5, "nombre": "EL CEDRO"},{"id": 6, "nombre": "EL TABLERO"},
        {"id": 7, "nombre": "LA GRANDEZA"},{"id": 8, "nombre": "MÁVIL"},
        {"id": 9, "nombre": "PIEDRA GRANDE"},{"id": 10, "nombre": "PROVINCIA CHIQUITA"},
        {"id": 11, "nombre": "SACUCHÚM"},{"id": 12, "nombre": "SAN ANDRÉS CHÁPIL"},
        {"id": 13, "nombre": "SAN ISIDRO CHAMAC"},{"id": 14, "nombre": "SAN JOSÉ CÁBEN"},
        {"id": 15, "nombre": "SAN PEDRO PETZ"},{"id": 16, "nombre": "SANTA TERESA"},
        {"id": 17, "nombre": "SAN FRANCISCO SOCHE"},
    ]
    # Eje seleccionado
    reportes = []
    queryReportes = Q()
    if request.method == "POST":
        generar_excel = request.POST.get('excel', False)
        eje_seleccionado = request.POST.get('eje', False)
        grupo_seleccionado = request.POST.get('grupo', False)
        identificador = request.POST.get('identificador', False)
        aldea = request.POST.get('aldea', False)
        responsable = request.POST.get('responsable', False)
        if eje_seleccionado == "0" and grupo_seleccionado == "0" and identificador == "0" and responsable == "0":
            reportes = ReporteGrupos.objects.all()
        else:
            # Si se selecciono Eje
            if eje_seleccionado != "0":
                queryReportes = queryReportes & Q(eje_trabajo = eje_seleccionado)
            # Si se selecciono Grupo
            if grupo_seleccionado != "0":
                queryReportes = queryReportes & Q(grupo = grupo_seleccionado)
            if identificador != "100":
                queryReportes = queryReportes & Q(grupo__identificador=identificador)
            if aldea != "0":
                queryReportes = queryReportes & Q(grupo__aldeas=aldea)
            if responsable != "0":
                queryReportes = queryReportes & Q(user__id=responsable)
            reportes = ReporteGrupos.objects.filter(queryReportes)
        # Generar excel
        export = []
        # Encabezados de excel
        export.append([
            'No.',
            'Grupo',
            'Proyecto',
            'Eje',
            'Beneficiados',
            'Presupuesto',
            'Fecha Inicio',
            'Fecha Finalización',
            'Encargado'
        ])
        count = 1
        for r in reportes:
            export.append([
                count,
                str(r.grupo),
                str(r.nombre_proyecto),
                str(r.eje_trabajo),
                str(r.beneficiados),
                str(r.presupuesto),
                str(r.fecha_inicio),
                str(r.fecha_finalizacion),
                str(r.user)
            ])
            count = count + 1
        today = datetime.now()
        strToday = today.strftime("%Y%m%d")
        # Transformar el array a un arreglo
        sheet = excel.pe.Sheet(export)
        return excel.make_response(sheet, "xlsx", file_name="reporteGrupos-"+strToday+".xlsx")
    else:
        return render(request,'reportes/grupos/admin.html', {'users': users, 'ejes': ejes, 'grupos': grupos, 'identificadores': identificadores, 'aldeas': aldeas, 'years':years})


@user_passes_test(administrador_check)
def reporte_servicios_admin(request):
    ejes = Eje.objects.all()
    users = Usuario.objects.all()
    tipos_servicio = [
        {"id": 0, "nombre": "CURSO"},
        {"id": 1, "nombre": "TALLER"},
        {"id": 2, "nombre": "SEMINARIO"},
        {"id": 3, "nombre": "DIPLOMADO"},
        {"id": 4, "nombre": "CAPACITACION"},
        {"id": 5, "nombre": "CONVERSATORIO"},
    ]
    queryReportes = Q()
    if request.method == "POST":
        eje_seleccionado = request.POST.get('eje', False)
        responsable = request.POST.get('responsable', False)
        servicio_seleccionado = request.POST.get('servicio_seleccionado', False)
        if eje_seleccionado == "-5" and responsable == "-5" and servicio_seleccionado == "-5":
            reportes = ReporteServicios.objects.all()
        else:
            # Si se selecciono Eje
            if eje_seleccionado != "-5":
                queryReportes = queryReportes & Q(eje_trabajo = eje_seleccionado)
            # Si se selecciono Servicio
            if servicio_seleccionado != "-5":
                queryReportes = queryReportes & Q(servicio__modalidad = servicio_seleccionado)
            if responsable != "-5":
                queryReportes = queryReportes & Q(user__id=responsable)
            reportes = ReporteServicios.objects.filter(queryReportes)
        return render(request,'reportes/servicios/admin.html', {'users': users, 'ejes': ejes, 'reportes': reportes, 'tipos_servicios': tipos_servicio})

    else:
        return render(request,'reportes/servicios/admin.html', {'users': users, 'ejes': ejes, 'tipos_servicios': tipos_servicio})

# Generar reporte en excel
@user_passes_test(administrador_check)
def reporte_servicios_admin_excel(request):
    ejes = Eje.objects.all()
    users = Usuario.objects.all()
    tipos_servicio = [
        {"id": 0, "nombre": "CURSO"},
        {"id": 1, "nombre": "TALLER"},
        {"id": 2, "nombre": "SEMINARIO"},
        {"id": 3, "nombre": "DIPLOMADO"},
        {"id": 4, "nombre": "CAPACITACION"},
        {"id": 5, "nombre": "CONVERSATORIO"},
    ]
    queryReportes = Q()
    if request.method == "POST":
        eje_seleccionado = request.POST.get('eje', False)
        responsable = request.POST.get('responsable', False)
        servicio_seleccionado = request.POST.get('servicio_seleccionado', False)
        if eje_seleccionado == "-5" and responsable == "-5" and servicio_seleccionado == "-5":
            reportes = ReporteServicios.objects.all()
        else:
            # Si se selecciono Eje
            if eje_seleccionado != "-5":
                queryReportes = queryReportes & Q(eje_trabajo = eje_seleccionado)
            # Si se selecciono Servicio
            if servicio_seleccionado != "-5":
                queryReportes = queryReportes & Q(servicio__modalidad = servicio_seleccionado)
            if responsable != "-5":
                queryReportes = queryReportes & Q(user__id=responsable)
            reportes = ReporteServicios.objects.filter(queryReportes)
        # Generar excel
        export = []
        # Encabezados de excel
        export.append([
            'No.',
            'Eje de trabajo',
            'Servicio',
            'Beneficiados',
            'Presupuesto',
            'Fecha Inicio',
            'Fecha Finalización',
            'Encargado'
        ])
        count = 1
        for r in reportes:
            export.append([
                count,
                str(r.eje_trabajo),
                str(r.servicio),
                str(r.beneficiados),
                str(r.presupuesto),
                str(r.fecha_inicio),
                str(r.fecha_finalizacion),
                str(r.user)
            ])
            count = count + 1
        today = datetime.now()
        strToday = today.strftime("%Y%m%d")
        # Transformar el array a un arreglo
        sheet = excel.pe.Sheet(export)
        return excel.make_response(sheet, "xlsx", file_name="reporteServicios-"+strToday+".xlsx")
        return render(request,'reportes/servicios/admin.html', {'users': users, 'ejes': ejes, 'reportes': reportes, 'tipos_servicios': tipos_servicio})

    else:
        return render(request,'reportes/servicios/admin.html', {'users': users, 'ejes': ejes, 'tipos_servicios': tipos_servicio})
#REPORTES VIEW
#REPORTES VIEW
#ESTADISTICA POR INVERSION
#ESTADISTICA POR BENEFICIARIOS
def get_data_inversion(request):
    labels = []
    data = []
    # Obtener campos para la consulta
    year = request.POST.get('year', False)
    identificador = request.POST.get('identificador', False)
    aldea = request.POST.get('aldea', False)
    canton = request.POST.get('canton', False)
    direccion = request.POST.get('direccion', False)
    if year != 0 and identificador != -1 and aldea != -1:
        # Si selecciono area rural
        if identificador == "0":
            # Busca aldeas
            queryset = ReporteGrupos.objects.filter(grupo_id__aldeas=aldea, created_on__year=year).values('eje_trabajo__eje_trabajo').annotate(presupuesto=Sum('presupuesto'))
        elif identificador == "1":
            # Busca cantones
            queryset = ReporteGrupos.objects.filter(grupo_id__canton=canton, created_on__year=year).values('eje_trabajo__eje_trabajo').annotate(presupuesto=Sum('presupuesto'))
        elif identificador == "2":
            # Busca general llano grande
            queryset = ReporteGrupos.objects.filter(grupo_id__direccion_alternativa=direccion, created_on__year=year).values('eje_trabajo__eje_trabajo').annotate(presupuesto=Sum('presupuesto'))
    for entry in queryset:
        labels.append(entry['eje_trabajo__eje_trabajo'])
        data.append(entry['presupuesto'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def estadistica_inversion(request):
    direcciones = Grupo.objects.all().values('direccion_alternativa').exclude(direccion_alternativa=None).distinct()
    ejes = Eje.objects.all()
    grupos = Grupo.objects.all()
    users = Usuario.objects.all()
    years = [
        {'id': 2021, "texto": "2021"},
        {'id': 2022, "texto": "2022"},
        {'id': 2023, "texto": "2023"},
        {'id': 2024, "texto": "2024"},
        {'id': 2025, "texto": "2025"},
        {'id': 2026, "texto": "2026"},
        {'id': 2027, "texto": "2027"},
        {'id': 2028, "texto": "2028"},
        {'id': 2029, "texto": "2029"},
        {'id': 2030, "texto": "2030"},
        {'id': 2031, "texto": "2031"},
    ]
    identificadores = [
        {'id': 0, 'tipo': 'AREA RURAL'},
        {'id': 1, 'tipo': 'AREA URBANA'},
        {'id': 2, 'tipo': 'LLANO GRANDE'}
    ]
    aldeas = [
        {"id": 1, "nombre": "CANTEL"}, {"id": 2, "nombre": "CORRAL GRANDE"},
        {"id": 3, "nombre": "CHAMPOLLAP"},{"id": 4, "nombre": "CHIM"},
        {"id": 5, "nombre": "EL CEDRO"},{"id": 6, "nombre": "EL TABLERO"},
        {"id": 7, "nombre": "LA GRANDEZA"},{"id": 8, "nombre": "MÁVIL"},
        {"id": 9, "nombre": "PIEDRA GRANDE"},{"id": 10, "nombre": "PROVINCIA CHIQUITA"},
        {"id": 11, "nombre": "SACUCHÚM"},{"id": 12, "nombre": "SAN ANDRÉS CHÁPIL"},
        {"id": 13, "nombre": "SAN ISIDRO CHAMAC"},{"id": 14, "nombre": "SAN JOSÉ CÁBEN"},
        {"id": 15, "nombre": "SAN PEDRO PETZ"},{"id": 16, "nombre": "SANTA TERESA"},
        {"id": 17, "nombre": "SAN FRANCISCO SOCHE"},
    ]
    cantones = [
        {"id": 1, "nombre": "LA PARROQUIA"}, {"id": 2, "nombre": "SANTA MARIA DE ATOCHA"},
        {"id": 3, "nombre": "SAN MIGUEL"},{"id": 4, "nombre": "SAN JUAN DE DIOS"},
        {"id": 5, "nombre": "SAN JUAN DEL POZO"},{"id": 6, "nombre": "SAN AGUSTÍN TONALÁ"},
        {"id": 7, "nombre": "EL MOSQUITO"},{"id": 8, "nombre": "SAN SEBASTIÁN"},
    ]
    # Eje seleccionado
    reportes = []
    return render(request,'reportes/charts/estadistica_inversion.html', {'users': users, 'ejes': ejes, 'grupos': grupos, 'identificadores': identificadores, 'aldeas': aldeas, 'years': years, 'cantones':cantones, 'direcciones': direcciones})

#ESTADISTICA POR BENEFICIARIOS
def get_data_beneficiarios(request):
    labels = []
    data = []
    # Obtener campos para la consulta
    year = request.POST.get('year', False)
    identificador = request.POST.get('identificador', False)
    aldea = request.POST.get('aldea', False)
    canton = request.POST.get('canton', False)
    direccion = request.POST.get('direccion', False)
    if year != 0 and identificador != -1 and aldea != -1:
        # Si selecciono area rural
        if identificador == "0":
            # Busca aldeas
            queryset = ReporteGrupos.objects.filter(grupo_id__aldeas=aldea, created_on__year=year).values('eje_trabajo__eje_trabajo').annotate(beneficiados=Sum('beneficiados'))
        elif identificador == "1":
            # Busca cantones
            queryset = ReporteGrupos.objects.filter(grupo_id__canton=canton, created_on__year=year).values('eje_trabajo__eje_trabajo').annotate(beneficiados=Sum('beneficiados'))
        elif identificador == "2":
            # Busca general llano grande
            queryset = ReporteGrupos.objects.filter(grupo_id__direccion_alternativa=direccion, created_on__year=year).values('eje_trabajo__eje_trabajo').annotate(beneficiados=Sum('beneficiados'))
    for entry in queryset:
        labels.append(entry['eje_trabajo__eje_trabajo'])
        data.append(entry['beneficiados'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def estadistica_beneficiarios(request):
    direcciones = Grupo.objects.all().values('direccion_alternativa').exclude(direccion_alternativa=None).distinct()
    ejes = Eje.objects.all()
    grupos = Grupo.objects.all()
    users = Usuario.objects.all()
    years = [
        {'id': 2021, "texto": "2021"},
        {'id': 2022, "texto": "2022"},
        {'id': 2023, "texto": "2023"},
        {'id': 2024, "texto": "2024"},
        {'id': 2025, "texto": "2025"},
        {'id': 2026, "texto": "2026"},
        {'id': 2027, "texto": "2027"},
        {'id': 2028, "texto": "2028"},
        {'id': 2029, "texto": "2029"},
        {'id': 2030, "texto": "2030"},
        {'id': 2031, "texto": "2031"},
    ]
    identificadores = [
        {'id': 0, 'tipo': 'AREA RURAL'},
        {'id': 1, 'tipo': 'AREA URBANA'},
        {'id': 2, 'tipo': 'LLANO GRANDE'}
    ]
    aldeas = [
        {"id": 1, "nombre": "CANTEL"}, {"id": 2, "nombre": "CORRAL GRANDE"},
        {"id": 3, "nombre": "CHAMPOLLAP"},{"id": 4, "nombre": "CHIM"},
        {"id": 5, "nombre": "EL CEDRO"},{"id": 6, "nombre": "EL TABLERO"},
        {"id": 7, "nombre": "LA GRANDEZA"},{"id": 8, "nombre": "MÁVIL"},
        {"id": 9, "nombre": "PIEDRA GRANDE"},{"id": 10, "nombre": "PROVINCIA CHIQUITA"},
        {"id": 11, "nombre": "SACUCHÚM"},{"id": 12, "nombre": "SAN ANDRÉS CHÁPIL"},
        {"id": 13, "nombre": "SAN ISIDRO CHAMAC"},{"id": 14, "nombre": "SAN JOSÉ CÁBEN"},
        {"id": 15, "nombre": "SAN PEDRO PETZ"},{"id": 16, "nombre": "SANTA TERESA"},
        {"id": 17, "nombre": "SAN FRANCISCO SOCHE"},
    ]
    cantones = [
        {"id": 1, "nombre": "LA PARROQUIA"}, {"id": 2, "nombre": "SANTA MARIA DE ATOCHA"},
        {"id": 3, "nombre": "SAN MIGUEL"},{"id": 4, "nombre": "SAN JUAN DE DIOS"},
        {"id": 5, "nombre": "SAN JUAN DEL POZO"},{"id": 6, "nombre": "SAN AGUSTÍN TONALÁ"},
        {"id": 7, "nombre": "EL MOSQUITO"},{"id": 8, "nombre": "SAN SEBASTIÁN"},
    ]
    # Eje seleccionado
    reportes = []
    return render(request,'reportes/charts/estadistica_beneficiario.html', {'users': users, 'ejes': ejes, 'grupos': grupos, 'identificadores': identificadores, 'aldeas': aldeas, 'years': years, 'cantones':cantones, 'direcciones': direcciones})

#ESTADISTICA POR GRUPOS
def get_data_grupos(request):
    years = [
        {'id': 2021, "texto": "2021"},
        {'id': 2022, "texto": "2022"},
        {'id': 2023, "texto": "2023"},
        {'id': 2024, "texto": "2024"},
        {'id': 2025, "texto": "2025"},
        {'id': 2026, "texto": "2026"},
        {'id': 2027, "texto": "2027"},
        {'id': 2028, "texto": "2028"},
        {'id': 2029, "texto": "2029"},
        {'id': 2030, "texto": "2030"},
        {'id': 2031, "texto": "2031"},
    ]
    aldeas = [
        {"id": 1, "nombre": "CANTEL"}, {"id": 2, "nombre": "CORRAL GRANDE"},
        {"id": 3, "nombre": "CHAMPOLLAP"},{"id": 4, "nombre": "CHIM"},
        {"id": 5, "nombre": "EL CEDRO"},{"id": 6, "nombre": "EL TABLERO"},
        {"id": 7, "nombre": "LA GRANDEZA"},{"id": 8, "nombre": "MÁVIL"},
        {"id": 9, "nombre": "PIEDRA GRANDE"},{"id": 10, "nombre": "PROVINCIA CHIQUITA"},
        {"id": 11, "nombre": "SACUCHÚM"},{"id": 12, "nombre": "SAN ANDRÉS CHÁPIL"},
        {"id": 13, "nombre": "SAN ISIDRO CHAMAC"},{"id": 14, "nombre": "SAN JOSÉ CÁBEN"},
        {"id": 15, "nombre": "SAN PEDRO PETZ"},{"id": 16, "nombre": "SANTA TERESA"},
        {"id": 17, "nombre": "SAN FRANCISCO SOCHE"},
    ]
    cantones = [
        {"id": 1, "nombre": "LA PARROQUIA"}, {"id": 2, "nombre": "SANTA MARIA DE ATOCHA"},
        {"id": 3, "nombre": "SAN MIGUEL"},{"id": 4, "nombre": "SAN JUAN DE DIOS"},
        {"id": 5, "nombre": "SAN JUAN DEL POZO"},{"id": 6, "nombre": "SAN AGUSTÍN TONALÁ"},
        {"id": 7, "nombre": "EL MOSQUITO"},{"id": 8, "nombre": "SAN SEBASTIÁN"},
    ]
    labels = []
    data = []
    # Obtener campos para la consulta
    year = request.POST.get('year', False)
    identificadorArea = request.POST.get('identificador', False)
    if year != 0 and identificadorArea != "-1":
        # Si selecciono area rural
        if identificadorArea == "0":
            # Busca aldeas
            queryset = Grupo.objects.filter(identificador=1, created_on__year=year).values('aldeas').annotate(total=Count(id))
            for entry in queryset:
                indx = int(entry['aldeas']) - 1
                labels.append(aldeas[indx]['nombre'])
                data.append(entry['total'])
        elif identificadorArea == "1":
            # Busca cantones
            queryset = Grupo.objects.filter(identificador=2, created_on__year=year).values('canton').annotate(total=Count(id))
            for entry in queryset:
                indx = int(entry['canton']) - 1
                labels.append(cantones[indx]['nombre'])
                data.append(entry['total'])
        elif identificadorArea == "2":
            # Busca general llano grande
            queryset = Grupo.objects.filter(identificador=3, created_on__year=year).values('direccion_alternativa').annotate(total=Count(id))
            for entry in queryset:
                labels.append(entry['direccion_alternativa'])
                data.append(entry['total'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def estadistica_grupos(request):
    grupos = Grupo.objects.all()
    users = Usuario.objects.all()
    years = [
        {'id': 2021, "texto": "2021"},
        {'id': 2022, "texto": "2022"},
        {'id': 2023, "texto": "2023"},
        {'id': 2024, "texto": "2024"},
        {'id': 2025, "texto": "2025"},
        {'id': 2026, "texto": "2026"},
        {'id': 2027, "texto": "2027"},
        {'id': 2028, "texto": "2028"},
        {'id': 2029, "texto": "2029"},
        {'id': 2030, "texto": "2030"},
        {'id': 2031, "texto": "2031"},
    ]
    identificadores = [
        {'id': 0, 'tipo': 'AREA RURAL'},
        {'id': 1, 'tipo': 'AREA URBANA'},
        {'id': 2, 'tipo': 'LLANO GRANDE'}
    ]
    aldeas = [
        {"id": 1, "nombre": "CANTEL"}, {"id": 2, "nombre": "CORRAL GRANDE"},
        {"id": 3, "nombre": "CHAMPOLLAP"},{"id": 4, "nombre": "CHIM"},
        {"id": 5, "nombre": "EL CEDRO"},{"id": 6, "nombre": "EL TABLERO"},
        {"id": 7, "nombre": "LA GRANDEZA"},{"id": 8, "nombre": "MÁVIL"},
        {"id": 9, "nombre": "PIEDRA GRANDE"},{"id": 10, "nombre": "PROVINCIA CHIQUITA"},
        {"id": 11, "nombre": "SACUCHÚM"},{"id": 12, "nombre": "SAN ANDRÉS CHÁPIL"},
        {"id": 13, "nombre": "SAN ISIDRO CHAMAC"},{"id": 14, "nombre": "SAN JOSÉ CÁBEN"},
        {"id": 15, "nombre": "SAN PEDRO PETZ"},{"id": 16, "nombre": "SANTA TERESA"},
        {"id": 17, "nombre": "SAN FRANCISCO SOCHE"},
    ]
    cantones = [
        {"id": 1, "nombre": "LA PARROQUIA"}, {"id": 2, "nombre": "SANTA MARIA DE ATOCHA"},
        {"id": 3, "nombre": "SAN MIGUEL"},{"id": 4, "nombre": "SAN JUAN DE DIOS"},
        {"id": 5, "nombre": "SAN JUAN DEL POZO"},{"id": 6, "nombre": "SAN AGUSTÍN TONALÁ"},
        {"id": 7, "nombre": "EL MOSQUITO"},{"id": 8, "nombre": "SAN SEBASTIÁN"},
    ]
    # Eje seleccionado
    reportes = []
    return render(request,'reportes/charts/estadistica_grupos.html', {'users': users, 'grupos': grupos, 'identificadores': identificadores, 'aldeas': aldeas, 'years': years, 'cantones':cantones})




