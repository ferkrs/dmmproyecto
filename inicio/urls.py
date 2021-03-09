from . import views
from .views import *
from django.urls import path, include

urlpatterns = [
    # Index Route
    path('', index, name='index'),
    # Authentication Routes
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout', views.logout_view, name='logout'),
    # User Routes
    path('users/list', views.user_list, name='user_list'),
    path('users/create', views.register, name='user_create'),
    path('users/update/<int:pk>', views.UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>', views.UserDeleteView.as_view(), name='user_delete'),
    # Personas Routes
    path('personas/list', views.personas_list, name='personas_list'),
    path('personas/update/<int:pk>', views.PersonaUpdateView.as_view(), name='personas_update'),
    #path('personas-delete/<int:id>', views.eliminar_persona, name='personas_delete'),
    # Grupos Routes
    path('grupos/add', grupo_crear, name='grupo_add'),
    path('grupos', grupo_crear, name='grupos'),
    path('grupos/list', grupo_list, name='grupo_list'),
    path('grupos/update/<int:pk>', views.GrupoUpdateView.as_view(), name='grupo_update'),
    path('grupos-delete/<int:id>', views.GrupoDelete, name='grupos_delete'),
    path('grupos/directiva/<int:id>', views.directiva, name='grupos_directiva'),
    # Asignacion de integrantes
    path('grupos/addpersonas/<int:id>', asignar_integrantes, name='pergrup_add'),
    path('grupos/addPersonas/<int:id>/integrantes/async', integrantes_grupo, name='pergrup_add_async'),
    path('grupos/addexistente/<int:id>', asignar_existente, name='pergrupexistente_add'),
    path('grupos/personas/delete/<int:id>/<int:grupo>', eliminar_integrante, name='pergrup_del'),
    path('grupos/personas/edit/<int:pk>', views.AsignacionUpdateView.as_view(), name='pergrup_update'),
    # Excel
    path('personas/excel', generar_excel, name='generar_excel'),
    path('grupos/personas/<int:id>/excel', integrantes_grupo_excel, name='grupo_integrantes_excel'),
    path('grupos/personas/directiva/<int:id>/excel', directiva_grupo_excel, name='grupo_directiva_excel')
]