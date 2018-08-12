from django.shortcuts import render
from .models import Gallery
# Create your views here.

def gallery(request):
    gallery = Gallery.objects
    return render(request, 'gallery.html', {'gallery': gallery})