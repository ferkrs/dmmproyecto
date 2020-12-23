from . import views
from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('grupos', grupos, name='grupos'),

]