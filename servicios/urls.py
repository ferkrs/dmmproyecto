from . import views
from .views import *
from django.urls import path

urlpatterns = [
    path('servicios/crear', servicio_crear, name='servicio_crear'),
    path('servicios/list', views.CursoList.as_view(), name='curso_list'),
    path('servicios/integrantes/<int:id>', views.servicio_integrantes, name="servicio_integrantes"),
    path('servicios/integrantes/<int:id>/<int:servicio>/delete', views.eliminar_integrante, name="servicio_integrantes_eliminar")
]