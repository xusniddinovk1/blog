from django.shortcuts import render, redirect
from .models import AboutSite, Category, Post


def contact(request):
    text = AboutSite.objects.all()
    ctx = {
        'text': text
    }
    return render(request, 'blog/about_site.html', ctx)


def home_page(request):
    categories = Category.objects.all()
    articles = Post.objects.all()
    ctx = {
        'categories': categories,
        'articles': articles
    }
    return render(request, 'blog/index.html', ctx)
