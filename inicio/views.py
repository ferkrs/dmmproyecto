from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse
from .models import *  
from .forms import GrupoForm
def index(request): 
    return render(request,'index.html')


class GruposAdd(generic.ListView):
    template_name =  'grupos/grupo_add.html'

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
    grupo = GrupoForm(request)
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            try:  
                form.save() 
                return render(request, 'grupos/grupos_add.html', {'grupo': grupo})
            except:  
                pass

    else:
        form = GrupoForm()
    return render(request, 'grupos/grupos_add.html', {'form': form})

#Asignar personas a grupos

#Grupo y personas del grupo

    #Funcion para renderizar dos modelos en un modelo
    #grupo = Grupo.objects.all()
    #relaciondpg = RelacionDPG.objects.all()
    #context= {'grupo': grupo, 'relaciondpg':relaciondpg}
    #return render(request, 'grupos/directiva.html', context)