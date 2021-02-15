from . import views
from .views import *
from django.urls import path, include

urlpatterns = [
    # User Routes
    path('alfabetizacion/list', views.comunidades_list, name='alfabetizacion_list'),
    path('alfabetizacion/crear', views.comunidad_create, name='alfabetizacion_create'),
    path('alfabetizacion/editar/<int:pk>', views.ComunidadUpdateView.as_view(), name='alfabetizacion_edit'),
    path('alfabetizacion/fases/crear/<int:id>', views.crear_fase, name='fases_crear'),
    path('alfabetizacion/fases/editar/<int:pk>', views.FaseUpdateView.as_view(), name='fases_edit'),
    path('alfabetizacion/fases/delete/<int:pk>', views.FaseDeleteView.as_view(), name='fases_delete'),
    path('alfabetizacion/fases/finalizar/<int:id>/<int:aprobados>', views.fase_finalizar, name='fases_finalizar'),
    path('alfabetizacion/fases/<int:id>/integrantes', views.integrantes_fase, name='fase_integrantes'),
    path('alfabetizacion/fases/<int:id>/existente', views.existente_fase, name='fase_existente'),
    path('alfabetizacion/fases/<int:id>/<int:grupo>/delete', views.eliminar_integrante, name='fase_integrantes_delete'),
    path('alfabetizacion/fases/<int:id>', views.comunidad_fases_list, name='alfabetizacion_fases'),
    # Excel
    path('alfabetizacion/fases/excel/<int:id>', views.fases_excel, name="alfabetizacion_fases_excel"),
    path('alfabetizacion/fases/<int:id>/integrantes/excel', views.integrantes_fase_excel, name="fase_integrantes_excel")
]