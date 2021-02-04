from django.contrib import admin
from .models import *
# Register your models here.
class EjeAdmin(admin.ModelAdmin):
    list_display = ('eje_trabajo'),
admin.site.register(Eje, EjeAdmin)