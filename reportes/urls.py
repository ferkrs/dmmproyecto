from . import views
from .views import *
from django.urls import path

urlpatterns = [
    path('reportegrupos/crear', reporte_grupo, name='reporte_grupo'),
    path('reportegrupos/delete/<int:id>', reporte_grupo_delete, name='reporte_grupo_delete'),
    path('reportegrupos/update/<int:pk>', ReporteGrupoUpdateView.as_view(), name='reporte_grupo_update'),
    path('reporteservicios/crear', reporte_servicio, name='reporte_servicio'),
    path('reporteservicios/delete/<int:id>', reporte_servicio_delete, name='reporte_servicio_delete'),
    path('reporteservicios/update/<int:pk>', ReporteServicioUpdateView.as_view(), name='reporte_servicio_update'),
    path('reporteservicios/crear', reporte_servicio, name='reporte_servicio'),
    path('reporte/grupos/admin', reporte_grupos_admin, name='reporte_grupos_admin'),
    path('reporte/grupos/admin/excel', reporte_grupos_admin_excel, name='reporte_grupos_admin_excel'),
    path('reporte/servicios/admin', reporte_servicios_admin, name='reporte_servicios_admin'),
    path('reporte/servicios/admin/excel', reporte_servicios_admin_excel, name='reporte_servicios_admin_excel')
]