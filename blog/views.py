from django.shortcuts import render, redirect
from .models import AboutSite, Category, Post


def home_page(request):
    categories = Category.objects.all()
    articles = Post.objects.all()
    ctx = {
        'categories': categories,
        'articles': articles
    }
    return render(request, 'blog/index.html', ctx)


def about_page(request):
    text = AboutSite.objects.first()
    ctx = {
        'text': text
    }
    return render(request, 'blog/about.html', ctx)
