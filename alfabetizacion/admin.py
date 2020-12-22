from django.contrib import admin
from .models import *
# Register your models here.
class MujeresAdmin(admin.ModelAdmin): 
    list_display = ('fase',)
    search_fields = ['fase']
    list_filter = ('fase',)
admin.site.register(MujeresAlfa, MujeresAdmin)

class ComunidadAdmin(admin.ModelAdmin): 
    list_display = ('comunidad',)
    search_fields = ['comunidad']
    list_filter = ('comunidad',)
admin.site.register(Comunidad, ComunidadAdmin)