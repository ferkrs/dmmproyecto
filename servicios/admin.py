from django.contrib import admin
from .models import *
# Register your models here.
class CursoAdmin(admin.ModelAdmin): 
    list_display = ('nombre',)
    search_fields = ['modalidad']
    list_filter = ('modalidad',)
admin.site.register(Curso, CursoAdmin)

