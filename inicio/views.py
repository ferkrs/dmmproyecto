from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView
from django.http import HttpResponse
from .models import *  
from .forms import GrupoForm
     
class GruposList(generic.ListView):
    queryset = Grupo.objects.all()
    template_name = 'grupos/grupos_list.html'
    
def grupo_crear(request):
    grupo = GrupoForm(request)
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            form = form.save()
            return render(request, 'grupos/grupos_add.html', {'grupo': grupo})
    else:
        form = GrupoForm()
    return render(request, 'grupos/grupos_add.html', {'form': form})


def index(request): 
    return render(request,'index.html')


# agregar el 
