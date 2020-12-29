from . import views
from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('grupos', grupo_crear, name='grupos'),
    path('grupos/list', views.GruposList.as_view(), name='grupo_list'),

]