from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = 'DMM Proyectos' 
 
class PersonaAdmin(admin.ModelAdmin): 
    list_display = ('cui',)
    search_fields = ['cui']
    list_filter = ('cui',)
admin.site.register(Persona, PersonaAdmin)

class CursoAdmin(admin.ModelAdmin): 
    list_display = ('nombre',)
    search_fields = ['modalidad']
    list_filter = ('modalidad',)
admin.site.register(Curso, CursoAdmin)


class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre_grupo',)
    search_fields = ['nombre_grupo']
    list_filter = ('nombre_grupo',)
admin.site.register(Grupo, GrupoAdmin)

class RelacionDPGAdmin(admin.ModelAdmin): 
    list_display = ('grupo','puesto')
    search_fields = ['puesto']
    list_filter = ('puesto',)
admin.site.register(RelacionDPG, RelacionDPGAdmin)