from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Animation
# Create your views here.

def index(request):
    return render(request, "home.html")


def Graph(request):
    Animations = Animation.objects.all()
    ctx = {
        'Animations': Animations
    }
    return render(request, 'Graph.html', ctx)

def about(request):
    return render(request, "about.html")
