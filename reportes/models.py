from django.db import models
from inicio.models import *
from servicios.models import *
from alfabetizacion.models import *

class Eje(models.Model):
    eje_trabajo = models.CharField(max_length=220,blank= False)
    def __str__(self):
        txt="{0}"
        return txt.format(self.eje_trabajo)

#reporte de grupos
class ReporteGrupos(models.Model):
    eje_trabajo = models.ForeignKey(Eje, on_delete= models.CASCADE,related_name='eje_grupos', null=False, blank=False)
    grupo = models.ForeignKey(Grupo, on_delete= models.CASCADE,related_name='grupo_id', null=False, blank=False)
    nombre_proyecto = models.CharField(max_length=100,blank= False)
    descripcion = models.CharField(max_length=150,blank= False)
    resultado= models.CharField(max_length=150,blank= False)
    beneficiados = models.IntegerField()
    presupuesto = models.DecimalField(max_digits=30, decimal_places=2)
    fecha_inicio = models.DateField(blank= True, null=True)
    fecha_finalizacion = models.DateField(blank= True, null=True)
    user = models.ForeignKey(Usuario, on_delete= models.CASCADE,related_name='usuario_grupo', null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

class ReporteServicios(models.Model):
    eje_trabajo = models.ForeignKey(Eje, on_delete= models.CASCADE,related_name='eje_servicios', null=False, blank=False)
    servicio = models.ForeignKey(Curso, on_delete= models.CASCADE,related_name='curso_id', null=False, blank=False)
    fecha_inicio = models.DateField(blank= True, null=True)
    fecha_finalizacion = models.DateField(blank= True, null=True)
    presupuesto = models.DecimalField(max_digits=30, decimal_places=2)
    descripcion = models.CharField(max_length=150,blank= False)
    beneficiados = models.IntegerField()
    resultado= models.CharField(max_length=150,blank= False)
    user = models.ForeignKey(Usuario, on_delete= models.CASCADE,related_name='usuario_servicio', null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)