from django.shortcuts import render
from .models import Banner

def home(request):
    banners = Banner.objects
    return render(request, 'home.html', {'banners': banners})

def history(request):
    return render(request, 'history.html')

def standards(request):
    return render(request, 'standards.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')