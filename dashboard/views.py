from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth import login, logout, authenticate

from blog.models import AboutSite, Category, Post
from dashboard.forms import AboutSiteForm, CategoryForm, PostForm, ProfileForm


def login_page(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        user = authenticate(phone_number=phone_number, password=password)
        if user:
            login(request, user)
            return redirect('main_dashboard')  # Login bo‘lsa, dashboardga yo‘naltiramiz
        else:
            return render(request, 'dashboard/login.html', {'error': 'Invalid credentials'})
    return render(request, 'dashboard/login.html')


@login_required(login_url='login_page')
def logout_page(request):
    logout(request)
    return redirect('login_page')


@login_required(login_url='login_page')
def my_profile(request):
    ctx = {'user': request.user}
    return render(request, 'dashboard/profile/profile.html', ctx)


@login_required(login_url='login_page')
def profile_edit(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('my_profile')
    else:
        form = ProfileForm(instance=user)

    return render(request, 'dashboard/profile/profile_edit.html', {'form': form})


@method_decorator(login_required(login_url='login_page'), name='dispatch')
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'dashboard/profile/password_change.html'
    success_url = reverse_lazy('password_change_done')


@login_required(login_url='login_page')
def main_dashboard(request):
    text = AboutSite.objects.first()
    categories = Category.objects.all()
    articles = Post.objects.all()

    ctx = {
        'count': {
            'text': len(text) if text else 0,
            'categories': len(categories),
            'articles': len(articles),
        }
    }
    return render(request, 'dashboard/index.html', ctx)


@login_required(login_url='login_page')
def about_list(request):
    text = AboutSite.objects.all()
    return render(request, 'dashboard/about/list.html', {'text': text})


@login_required(login_url='login_page')
def create_text(request):
    form = AboutSiteForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('about_list')
    return render(request, 'dashboard/about/form.html', {'form': form})


@login_required(login_url='login_page')
def edit_text(request, slug):
    form = AboutSiteForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('about_list')
    return render(request, 'dashboard/about/form.html', {'form': form})


@login_required(login_url='login_page')
def delete_text(request, slug):
    AboutSite.objects.get(slug=slug).delete()
    return redirect('about_list')


@login_required(login_url='login_page')
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'dashboard/category/list.html', {'categories': categories})


@login_required(login_url='login_page')
def create_category(request):
    form = CategoryForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'dashboard/category/form.html', {'form': form})


@login_required(login_url='login_page')
def edit_category(request, slug):
    form = CategoryForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'dashboard/category/form.html', {'form': form})


@login_required(login_url='login_page')
def delete_category(request, slug):
    Category.objects.get(slug=slug).delete()
    return redirect('category_list')


@login_required(login_url='login_page')
def article_list(request):
    posts = Post.objects.all()
    return render(request, 'dashboard/article/list.html', {'posts': posts})


@login_required(login_url='login_page')
def create_article(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('article_list')
    return render(request, 'dashboard/article/form.html', {'form': form})


@login_required(login_url='login_page')
def edit_article(request, slug):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('article_list')
    return render(request, 'dashboard/article/form.html', {'form': form})


@login_required(login_url='login_page')
def delete_article(request, slug):
    Post.objects.get(slug=slug).delete()
    return redirect('article_list')
