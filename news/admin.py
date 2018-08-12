from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'body')
    list_display_links = ('id', 'title', 'date', 'body')
    search_fields = ['id', 'title', 'date', 'body']
    ordering = ['id']

    fields = ('title',
              ('image', 'attachment'),
              'date',
              'body')
    save_on_top = True

admin.site.register(Article, ArticleAdmin)