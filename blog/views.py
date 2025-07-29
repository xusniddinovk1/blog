from django.shortcuts import render, redirect, get_object_or_404
from .models import AboutSite, Category, Post
from bs4 import BeautifulSoup

def home_page(request):
    articles = Post.objects.all()
    ctx = {
        'articles': articles
    }
    return render(request, 'blog/index.html', ctx)


def about_page(request):
    text = AboutSite.objects.first()
    ctx = {
        'text': text
    }
    return render(request, 'blog/about.html', ctx)


def article_page(request):
    categories = Category.objects.all()
    articles = Post.objects.all()
    ctx = {
        'articles': articles,
        'categories': categories
    }
    return render(request, 'blog/article.html', ctx)


def article_detail(request, slug):
    article = get_object_or_404(Post, slug=slug)

    soup = BeautifulSoup(article.content, 'html.parser')
    headings = []
    count = 1
    for tag in soup.find_all(['h2', 'h3']):
        tag['id'] = f'section-{count}'
        headings.append(tag.get_text())
        count += 1

    article.content = str(soup)

    return render(request, 'blog/article_detail.html', {
        'article': article,
        'toc': headings
    })
