from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = 'DMM Proyectos' 
 
class PersonaAdmin(admin.ModelAdmin): 
    list_display = (
                    'cui','primer_nombre', 
                    'segundo_nombre','primer_apellido', 
                    'segundo_apellido','fecha_nacimiento')
    search_fields = ['cui']
    list_filter = ('cui',)
admin.site.register(Persona, PersonaAdmin)

class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre_grupo','directiva_grupo')
    search_fields = ['nombre_grupo']
    list_filter = ('nombre_grupo',)
admin.site.register(Grupo, GrupoAdmin)

class RelacionDPGAdmin(admin.ModelAdmin): 
    list_display = ('grupo','puesto','persona_puesto')
    search_fields = ['puesto']
    list_filter = ('puesto',)
admin.site.register(RelacionDPG, RelacionDPGAdmin)