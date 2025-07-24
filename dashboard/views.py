from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from blog.models import AboutSite, Category, Post
from dashboard.forms import AboutSiteForm, CategoryForm, PostForm
from django.contrib.auth import login, logout, authenticate


def login_required_decorator(func):
    return login_required(login_url='login_page')


def login_page(request):
    if request.POST:
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        user = authenticate(phone_number=phone_number, password=password)
        if user:
            login(request, user)
        else:
            return render(request, 'dashboard/login.html', {'error': 'Invalid credentials'})
    return render(request, 'dashboard/login.html')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('login_page')


@login_required_decorator
def main_dashboard(request):
    text = AboutSite.objects.first()
    categories = Category.objects.all()
    articles = Post.objects.all()

    ctx = {
        'count': {
            'text': len(text),
            'categories': len(categories),
            'articles': len(articles),
        }
    }
    return render(request, 'dashboard/index.html', ctx)