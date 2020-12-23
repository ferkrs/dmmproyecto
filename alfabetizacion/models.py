from django.db import models
from inicio.models import Persona

class Comunidad(models.Model): 
    comunidad = models.CharField(max_length=30, blank=False)
    class Meta:
        verbose_name = "Agregar Comunidades"
        verbose_name_plural = "Agregar Comunidades"
    def __str__(self):
        return self.comunidad
class MujeresAlfa(models.Model):
    comunidad = models.ForeignKey(Comunidad, verbose_name="comunidades", on_delete = models.CASCADE)
    nombre_alfabetizadora = models.CharField(max_length=20, blank=False) 
    ciclo = models.DateField(blank=False)
    integrantes = models.ManyToManyField(Persona)
    FASE=[ 
        (0, "FASE INCIAL"), 
        (1, "PRIMERA DE POST"), 
        (2, "SEGUNDA DE POST"),
    ]
    fase = models.IntegerField(choices=FASE, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    class Meta:
        verbose_name = "Grupos de alfabetizacion"
        verbose_name_plural = "Grupos de alfabetizacion" 