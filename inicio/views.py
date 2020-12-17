from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView
from django.http import HttpResponse
from .models import * 

def index(request): 
    return render(request,'index.html')
