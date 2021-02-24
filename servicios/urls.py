from . import views
from .views import *
from django.urls import path

urlpatterns = [
    path('servicios/crear', servicio_crear, name='servicio_crear'),
    path('servicios/list', servicio_list, name='servicio_list'),
    path('servicios/update/<int:pk>', ServicioUpdateView.as_view(), name='servicio_update'),
    path('servicios/integrantes/<int:id>', views.servicio_integrantes, name="servicio_integrantes"),
    path('servicios/existentes/<int:id>', servicio_existente, name="servicio_existentes"),
    path('servicios/integrantes/<int:id>/<int:servicio>/delete', views.eliminar_integrante, name="servicio_integrantes_eliminar"),
    path('servicios-delete/<int:id>', views.ServicioDelete, name='servicio_delete'),
    # Excel
    path('servicios/integrantes/<int:id>/excel', views.integrantes_servicio_excel, name='integrantes_servicio_excel'),
]