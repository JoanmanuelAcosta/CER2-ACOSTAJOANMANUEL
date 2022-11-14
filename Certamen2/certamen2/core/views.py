from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path, include
from django.template.loader import get_template
from core.models import correspondencia , residencia




def index(request):
    paquete = correspondencia.objects.all()
    return render(request,'core/index.html', {"paquetes": paquete})
    
