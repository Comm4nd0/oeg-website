from django.contrib import admin
from .models import Banner


class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'url')
    list_display_links = ('id', 'title', 'text', 'url')
    search_fields = ['id', 'title', 'text', 'url']
    ordering = ['id']

    fields = ('title',
              'image',
              'text',
              'url')
    save_on_top = True

admin.site.register(Banner, BannerAdmin)