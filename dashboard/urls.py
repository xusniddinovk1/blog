from django.urls import path
from .views import *

urlpatterns = [
    path('', main_dashboard, name='main_dashboard'),
    path('login/', logout_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),

    path('aboutSite/', about_list, name='about_list'),
    path('aboutSite/create/', create_text, name='create_text'),
    path('aboutSite/<slug:slug>/edit', edit_text, name='edit_text'),
    path('aboutSite/<slug:slug>/delete', delete_text, name='delete_text'),

    path('category/', category_list, name='category_list'),
    path('category/create/', create_category, name='create_category'),
    path('category/<slug:slug>/edit', edit_category, name='edit_category'),
    path('category/<slug:slug>/delete', delete_category, name='delete_category'),

    path('articles/', article_list, name='article_list'),
    path('articles/create/', create_article, name='create_article'),
    path('articles/<slug:slug>/edit', edit_article, name='edit_article'),
    path('articles/<slug:slug>/delete', delete_article, name='delete_article'),
]
