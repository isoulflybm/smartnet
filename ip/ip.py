from django.shortcuts import render

from django.urls import path
from django.http import HttpResponse

from helpers.ip.ip4 import firewall

# Create your views here.

def index(request):
    return HttpResponse("Главная страница server")

urls = [
    path('', index)
]
