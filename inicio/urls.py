from . import views
from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('grupos/add', grupo_crear, name='grupo_add'),
    path('grupos/list', views.GruposList.as_view(), name='grupo_list'),
    path('grupos/addpersonas', GruposAdd, name='pergrup_add'),
    path('grupos-delete/<int:id>', views.GrupoDelete, name='grupos_delete'),
    path('grupos-directiva/<int:id>', views.DirectivaId, name='grupos_directiva'),

    
]