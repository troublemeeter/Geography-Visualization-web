from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Animation
# 定义视图

def index(request):
    return render(request, "cover.html")

def Graph1(request):
    return render(request, 'airline1.html')

def Graph2(request):
    return render(request, 'airline2.html')

def about(request):
    return render(request, "about2.html")
