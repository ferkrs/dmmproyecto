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
from django.http import HttpResponse
from .models import *  
from .forms import GrupoForm, RegisterForm, UserModelForm
from django.contrib import messages
# Bootstrap Modals
from bootstrap_modal_forms.generic import (
    BSModalDeleteView,
    BSModalUpdateView
)

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
    return render(request, 'users/user_list.html', {'usuarios': usuarios})

# User Delete
class UserDeleteView(BSModalDeleteView):
    model = Usuario
    template_name = 'users/user_delete.html'
    success_message = 'Success: El usuario ha sido eliminado correctamente'
    success_url = reverse_lazy('user_list')

# User Update
class UserUpdateView(BSModalUpdateView):
    model = Usuario
    template_name = 'users/user_edit.html'
    form_class = UserModelForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('user_list')

# User Create
@login_required
@user_passes_test(administrador_check)
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            return redirect('user_list')
    else:
        form = RegisterForm()
    return render(request, 'users/user_register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('accounts/login')

""" 

*****    VISTAS GRUPOS    *****

"""

def GruposAdd(request, id):
    grupo = Grupo.objects.get(id=id)
    return render(request,'grupos/grupo_add.html', {'grupo': grupo})

#funcion de listar
class GruposList(generic.ListView):
    queryset = Grupo.objects.all()
    template_name = 'grupos/grupos_list.html'

    def contar():
        id = Grupo.objects.filter(id)

        realacion = RelacionDPG.objects.filter(grupo=id).count()

#funcion de consulta de directiva by id
def DirectivaId(request, id): 
    datos = RelacionDPG.objects.filter(grupo=id).order_by('puesto')
    return render(request, 'grupos/directiva.html', {'datos': datos})

#Funcion de borrar  
def GrupoDelete(request, id):
    grupo = Grupo.objects.get(id=id)
    #Falta agregar la concicion de que el usuario esta seguro de borrar
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
                messages.success(request,"Se ha creado el grupo")
                return render(request, 'grupos/grupos_add.html', {'grupo': grupo})
            except:  
                pass
    else:
        form = GrupoForm()
    return render(request, 'grupos/grupos_add.html', {'form': form})
