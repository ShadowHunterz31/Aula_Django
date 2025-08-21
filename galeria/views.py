from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Alura Space</h1> <p> bem vindo ao espaço sideral</p>')
