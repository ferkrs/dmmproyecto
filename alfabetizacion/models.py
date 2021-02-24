from django.db import models
from inicio.models import Persona

# Modelo Comunidad
class Comunidad(models.Model):
    # Nombre de la comunidad
    comunidad = models.CharField(max_length=50, blank=False)
    class Meta:
        verbose_name = "Agregar Comunidades"
        verbose_name_plural = "Agregar Comunidades"
    def __str__(self):
        return self.comunidad

# Modelo MujeresAlfa
class MujeresAlfa(models.Model):
    # Nombre de la comunidad
    comunidad = models.ForeignKey(Comunidad, verbose_name="comunidades", on_delete = models.CASCADE)
    # Nombre encargada
    nombre_alfabetizadora = models.CharField(max_length=100, blank=False)
    # Ciclo
    ciclo = models.DateField(blank=False)
    # Integrantes
    integrantes = models.ManyToManyField(Persona, related_name="persona_alfabetizacion")
    # Fase de alfabetizacion
    FASE=[
        (0, "FASE INCIAL"),
        (1, "PRIMERA DE POST"),
        (2, "SEGUNDA DE POST"),
    ]
    fase = models.IntegerField(choices=FASE, null=False, blank=False)
    # Fechas de creacion y actualizacion
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    finalizado = models.BooleanField(default=False)
    aprobados = models.SmallIntegerField(default=0)

    class Meta:
        verbose_name = "Grupos de alfabetizacion"
        verbose_name_plural = "Grupos de alfabetizacion"