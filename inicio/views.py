# Auth imports
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
# Url Imports
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView, TemplateView
from django.urls import resolve
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Count
from django.core.paginator import Paginator
# Modelos
from .models import *
# Formularios
from .forms import (
    GrupoForm,
    RegisterForm,
    UserModelForm,
    PersonaForm,
    PersonaModalForm,
    AsignacionPersonaGrupoForm,
    AsignacionExistenteGrupoForm,
    AsignacionPersonaModal,
    GrupoModalForm
)
from django.contrib import messages
from django.views.defaults import page_not_found
# Bootstrap Modals
from bootstrap_modal_forms.generic import (
    BSModalDeleteView,
    BSModalUpdateView
)
# EXCEL
import django_excel as excel

# 404

def mi_error_404(request, exception):
    return page_not_found(request, '404.html')

# Index view
@login_required
def index(request):
    return render(request,'index.html')

"""

*****    VISTAS USERS    *****

"""
# Verifica si el rol del usuario autenticado es administrador
def administrador_check(user):
    if(user.rol == 0):
        return True
    else:
        return False

# Users List
@login_required
@user_passes_test(administrador_check)
def user_list(request):
    usuarios = Usuario.objects.all()
    paginator = Paginator(usuarios,10)
    page_number=request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'users/user_list.html', context={'usuarios': usuarios, 'usuarios': page_obj})

# User Delete
class UserDeleteView(BSModalDeleteView):
    model = Usuario
    template_name = 'users/user_delete.html'
    success_message = 'El usuario ha sido eliminado correctamente'
    success_url = reverse_lazy('user_list')

# User Update
class UserUpdateView(BSModalUpdateView):
    model = Usuario
    template_name = 'users/user_edit.html'
    form_class = UserModelForm
    success_message = 'El usuario fue editado correctamente.'
    success_url = reverse_lazy('user_list')

# User Create
@login_required
@user_passes_test(administrador_check)
def register(request):
    if request.method == 'POST':
        try:
            form = RegisterForm(request.POST)
            # Comprobar que el nombre de usuario sea único
            username = request.POST.get('username', False)
            if Usuario.objects.filter(username=username).count() > 0:
                messages.error(request, "Ya existe este usuario en el sistema, intente otra vez.")
                return redirect('user_create')
            if form.is_valid():
                user = form.save(commit=False)
                user.password = make_password(user.password)
                user.save()
                messages.success(request, "Usuario creado correctamente.")
                return redirect('user_list')
            else:
                # Si ocurre error en el server
                messages.error(request, "Ha ocurrido un error, vuelva a intentar.")
                return redirect('user_create')
        except Exception as e:
            print(e)
            return redirect('user_list')
    else:
        form = RegisterForm()
        return render(request, 'users/user_register.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts/login')

"""

*****    VISTAS PERSONAS    *****

"""
@login_required
def personas_list(request):
    personas_noasignadas = Persona.objects.filter()
    personas_asignadas = Persona.objects.exclude()
    paginator = Paginator(personas_asignadas,10)
    page_number=request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'personas/personas_list.html', context={'asignadas': personas_asignadas, 'no_asignadas': personas_noasignadas, 'asignadas':page_obj})


class PersonaUpdateView(BSModalUpdateView):
    model = Persona
    template_name = 'personas/personas_edit.html'
    form_class = PersonaModalForm
    success_message = 'La información fue editada correctamente.'
    success_url = reverse_lazy('personas_list')

#funcion de listar
@login_required
def grupo_list(request):
    grupos = Grupo.objects.annotate(num_integrantes=Count('grupo_directiva__persona'))
    formularioGrupo = GrupoForm
    paginator = Paginator(grupos,10)
    page_number=request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'grupos/grupos_list.html', {'grupos': grupos, 'formularioGrupo': formularioGrupo,'grupos':page_obj})

#funcion de consulta de directiva by id
@login_required
def directiva(request, id):
    datos = AsignacionPersonaGrupo.objects.filter(grupo=id).order_by('puesto')
    grupo_actual = Grupo.objects.get(pk=id)
    return render(request, 'grupos/directiva.html', {'datos': datos, 'grupo': grupo_actual})

#Funcion de borrar
@login_required
def GrupoDelete(request, id):
    grupo = Grupo.objects.get(id=id)
    try:
        grupo.delete()
    except:
        pass
    return redirect('grupo_list')
#Grupo Crear
def grupo_crear(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,"Grupo creado correctamente")
            except:
                pass
        return redirect('grupo_list')


class GrupoUpdateView(BSModalUpdateView):
    model = Grupo
    template_name = 'grupos/grupo_edit.html'
    form_class = GrupoModalForm
    success_message = 'Grupo editado correctamente.'
    success_url = reverse_lazy('grupo_list')
"""

*****    VISTAS ASIGNACION DE INTEGRANTES    *****

"""

# Crear persona y asignarlo a un grupo
@login_required
def asignar_integrantes(request, id):
    puestos = [
        {"value": 0, "nombre": "MIEBRO"},
        {"value": 1, "nombre": "PRESIDENTE"},
        {"value": 2, "nombre": "VICE-PRESIDENTE"},
        {"value": 3, "nombre": "SECRETARIA"},
        {"value": 4, "nombre": "TESORERA"},
        {"value": 5, "nombre": "VOCAL 1"},
        {"value": 6, "nombre": "VOCAL 2"},
        {"value": 7, "nombre": "VOCAL 3"},
        {"value": 8, "nombre": "VOCAL 4"}
    ]
    if request.method == "POST":
        try:
            # Form de Persona
            formPersona = PersonaForm(request.POST)
            # Form de Asignacion
            formAsignacion = AsignacionPersonaGrupoForm(request.POST)
            # Instancia de grupo actual
            grupo_actual = Grupo.objects.get(id=id)
            # Validar si ya existe persona con mismo dpi
            if Persona.objects.filter(cui=formPersona['cui'].value()).count() > 0:
                messages.success(request, "Ya existe este una persona con este DPI, intente otra vez.")
                return redirect('/grupos/addpersonas/'+ str(grupo_actual.id))
            # Si los forms estan correctos
            if  formAsignacion.is_valid() and formPersona.is_valid():
                # Se crea y guarda la persona
                persona_creada = formPersona.save()
                # Se crea la asignacion con persona, puesto y grupo
                AsignacionPersonaGrupo.objects.create(persona = persona_creada, puesto=request.POST['puesto'], grupo=grupo_actual)
                return redirect('/grupos/addpersonas/'+ str(grupo_actual.id))
        except Exception as e:
            print(e)
            return redirect('/grupos/addpersonas/'+ str(grupo_actual.id))
    else:
        personas = Persona.objects.filter(persona_directiva=None)
        formPersona = PersonaForm
        formExistente = AsignacionExistenteGrupoForm
        asignacion = AsignacionPersonaGrupoForm
        grupo_actual = Grupo.objects.get(id=id)
        integrantes = AsignacionPersonaGrupo.objects.filter(grupo=grupo_actual)
        print(integrantes)
        return render(request,'grupos/grupo_add.html', {'formExistente': formExistente, 'grupo': grupo_actual, 'formPersona': formPersona, 'formAsignacion': asignacion, 'integrantes': integrantes, 'personas': personas, 'puestos': puestos})

@login_required
def asignar_existente(request, id):
    if request.method == "POST":
        try:
            persona = request.POST.get('existente', False)
            puesto = request.POST.get('ppExistente', False)
            grupo_actual = Grupo.objects.get(id=id)
            # Si los forms estan correctos
            if persona != False and puesto != False:
                personaEncontrada = Persona.objects.get(pk=persona)
                AsignacionPersonaGrupo.objects.create(persona=personaEncontrada, puesto=puesto, grupo=grupo_actual)
                message.success("Integrado asignado correctamente.")
                return redirect('/grupos/addpersonas/'+ str(grupo_actual.id))
            else:
                message.error("Datos invalidos")
                print("No valido")
                return redirect('/grupos/addpersonas/'+ str(grupo_actual.id))
        except Exception as e:
            print(e)
            return redirect('/grupos/addpersonas/'+ str(grupo_actual.id))
    else:
        formPersona = PersonaForm
        formExistente = AsignacionExistenteGrupoForm
        asignacion = AsignacionPersonaGrupoForm
        grupo_actual = Grupo.objects.get(id=id)
        integrantes = AsignacionPersonaGrupo.objects.filter(grupo=grupo_actual)
        return render(request,'grupos/grupo_add.html', {'formExistente': formExistente, 'grupo': grupo_actual, 'formPersona': formPersona, 'formAsignacion': asignacion, 'integrantes': integrantes})

@login_required
def eliminar_integrante(request, id, grupo):
    # Obtener relacion
    integrante = AsignacionPersonaGrupo.objects.filter(id=id)
    try:
        integrante.delete()
    except:
        pass
    return redirect('/grupos/addpersonas/'+str(grupo))

# User Update
class AsignacionUpdateView(BSModalUpdateView):
    model = AsignacionPersonaGrupo
    template_name = 'grupos/asignacion_edit.html'
    form_class = AsignacionPersonaModal
    success_message = 'Success: El usuario fue editado correctamente.'
    success_url = reverse_lazy('grupo_list')


"""
    GENERACION A EXCEL
"""
@login_required
def generar_excel(request):
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
        'Dirección',
        'Teléfono',
        'Correo Electronico',
    ])
    # Obtener registros del modelo
    personas = Persona.objects.all()
    count = 1
    for persona in personas:
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
            persona.direccion,
            persona.telefono,
            persona.correo_electronico,
        ])
        count = count + 1
    today = datetime.now()
    strToday = today.strftime("%Y%m%d")

    # Transformar el array a un arreglo
    sheet = excel.pe.Sheet(export)

    return excel.make_response(sheet, "xlsx", file_name="personas-"+strToday+".xlsx")

@login_required
def integrantes_grupo_excel(request, id):
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
        'Correo Electronico'
    ])
    # Obtener registros del modelo
    grupo_actual = Grupo.objects.get(id=id)
    integrantes = AsignacionPersonaGrupo.objects.filter(grupo=grupo_actual)
    count = 1
    for integrante in integrantes:
        export.append([
            count,
            integrante.persona.cui,
            integrante.persona.get_sexo_display(),
            integrante.persona.primer_nombre,
            integrante.persona.segundo_nombre,
            integrante.persona.tercer_nombre,
            integrante.persona.primer_apellido,
            integrante.persona.segundo_apellido,
            integrante.persona.apellido_casada,
            str(integrante.persona.fecha_nacimiento),
            integrante.persona.direccion,
            integrante.persona.correo_electronico,
        ])
        count = count + 1
    today = datetime.now()
    strToday = today.strftime("%Y%m%d")

    # Transformar el array a un arreglo
    sheet = excel.pe.Sheet(export)

    return excel.make_response(sheet, "xlsx", file_name="integrantes-"+grupo_actual.nombre_grupo+"-"+strToday+".xlsx")

@login_required
def directiva_grupo_excel(request, id):
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
        'Correo Electronico',
        'Telefono',
        'Puesto',
    ])
    # Obtener registros del modelo
    grupo_actual = Grupo.objects.get(id=id)
    integrantes = AsignacionPersonaGrupo.objects.filter(grupo=grupo_actual).exclude(puesto=0).order_by('puesto')
    count = 1
    for integrante in integrantes:
        export.append([
            count,
            integrante.persona.cui,
            integrante.persona.get_sexo_display(),
            integrante.persona.primer_nombre,
            integrante.persona.segundo_nombre,
            integrante.persona.tercer_nombre,
            integrante.persona.primer_apellido,
            integrante.persona.segundo_apellido,
            integrante.persona.apellido_casada,
            str(integrante.persona.fecha_nacimiento),
            integrante.persona.correo_electronico,
            integrante.persona.telefono,
            integrante.get_puesto_display()
        ])
        count = count + 1
    today = datetime.now()
    strToday = today.strftime("%Y%m%d")

    # Transformar el array a un arreglo
    sheet = excel.pe.Sheet(export)

    return excel.make_response(sheet, "xlsx", file_name="directiva-"+grupo_actual.nombre_grupo+"-"+strToday+".xlsx")

