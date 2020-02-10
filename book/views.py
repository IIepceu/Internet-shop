from django.shortcuts import render
from django.http import HttpResponse
# Create your views here

def homepage(request):
    return HttpResponse('Главная страница')

def protein_page(request):
    return HttpResponse('Страница с протеином')

def geiner_page(request):
    return HttpResponse('Страница с гейнером')

def bcaa_page(request):
    return HttpResponse('Страница с бсаа')

def creatin_page(request):
    return HttpResponse('Страница с креатином')

def information_page(request):
    return HttpResponse('Страница с инофрмацией о спорт-пите')