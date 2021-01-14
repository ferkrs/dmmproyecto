from . import views
from .views import *
from django.urls import path, include

urlpatterns = [
    path('', index, name='index'),
    # User Routes
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/create', views.register, name='user_create'),
    path('users/list', views.user_list, name='user_list'),
    path('logout', views.logout_view, name='logout'),
    # Grupos Routes
    path('grupos', grupo_crear, name='grupos'),
    path('grupos/list', views.GruposList.as_view(), name='grupo_list'),
    path('grupos/add', views.GruposAdd.as_view(), name='grupo_add'),
    path('grupos-delete/<int:id>', views.GrupoDelete, name='grupos_delete'),
    path('grupos-directiva/<int:id>', views.DirectivaId, name='grupos_directiva'),   
]