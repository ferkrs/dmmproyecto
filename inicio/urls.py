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
    # Grupos Routes
    path('grupos/add', grupo_crear, name='grupo_add'),
    path('grupos', grupo_crear, name='grupos'),
    path('grupos/list', views.GruposList.as_view(), name='grupo_list'),
    path('grupos/addpersonas/<int:id>', GruposAdd, name='pergrup_add'),
    path('grupos-delete/<int:id>', views.GrupoDelete, name='grupos_delete'),
    path('grupos-directiva/<int:id>', views.DirectivaId, name='grupos_directiva'),   
]