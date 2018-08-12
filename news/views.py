from django.shortcuts import render
from .models import Article
# Create your views here.

def news(request):
    news_articles = Article.objects
    return render(request, 'news.html', {'news_articles': news_articles})