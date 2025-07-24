from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

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
def my_profile(request):
    ctx = {
        'user': request.user,
    }
    return render(request, 'dashboard/profile/profile.html', ctx)


@login_required_decorator
def profile_edit(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('my_profile')  # profil sahifasiga qaytish
    else:
        form = ProfileForm(instance=user)

    ctx = {
        'form': form
    }

    return render(request, 'dashboard/profile/profile_edit.html', ctx)


@method_decorator(login_required, name='dispatch')
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'dashboard/profile/password_change.html'
    success_url = reverse_lazy('password_change_done')


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


@login_required_decorator
def about_list(request):
    text = AboutSite.objects.all()
    ctx = {
        'text': text
    }
    return render(request, 'dashboard/about/list.html', ctx)


@login_required_decorator
def create_text(request):
    model = AboutSite()
    form = AboutSiteForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('about_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/about/form.html', ctx)


@login_required_decorator
def edit_text(request, slug):
    model = AboutSite.objects.get(slug=slug)
    form = AboutSiteForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('about_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/about/form.html', ctx)


@login_required_decorator
def delete_text(request, slug):
    model = AboutSite.objects.get(slug=slug)
    model.delete()
    return redirect('about_list')


@login_required_decorator
def category_list(request):
    categories = Category.objects.all()
    ctx = {
        'categories': categories
    }
    return render(request, 'dashboard/category/list.html', ctx)


@login_required_decorator
def create_category(request):
    model = Category()
    form = CategoryForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('category_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/category/form.html', ctx)


@login_required_decorator
def edit_category(request, slug):
    model = Category.objects.get(slug=slug)
    form = CategoryForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('category_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/category/form.html', ctx)


@login_required_decorator
def delete_category(request, slug):
    model = Category.objects.get(slug=slug)
    model.delete()
    return redirect('category_list')


@login_required_decorator
def article_list(request):
    posts = Post.objects.all()
    ctx = {
        'posts': posts
    }
    return render(request, 'dashboard/article/list.html', ctx)


@login_required_decorator
def create_article(request):
    model = Post()
    form = PostForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('article_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/article/form.html', ctx)


@login_required_decorator
def edit_article(request, slug):
    model = Post.objects.get(slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('article_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/article/form.html', ctx)


@login_required_decorator
def delete_article(request, slug):
    model = Post.objects.get(slug=slug)
    model.delete()
    return redirect('article_list')
