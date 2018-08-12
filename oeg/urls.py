from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
                  path('admin/', admin.site.urls, name='admin'),
                  path('', views.home, name='home'),
                  path('pedigree/', include('pedigree.urls')),
                  path('news/', include('news.urls')),
                  path('gallery/', include('gallery.urls')),
                  path('history/', views.history, name='history'),
                  path('standards/', views.standards, name='standards'),
                  path('about/', views.about, name='about'),
                  path('contact/', views.contact, name='contact'),
                  path('members/', include('members.urls')),
                  path('tinymce/', include('tinymce.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
