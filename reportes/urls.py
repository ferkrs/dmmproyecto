from . import views
from .views import *
from django.urls import path

urlpatterns = [
    path('reportegrupos/crear', reporte_grupo, name='reporte_grupo'),
    path('reporteservicios/crear', reporte_servicio, name='reporte_servicio'),

]