from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('about/', about_page, name='about_page'),
    path('article/', article_page, name='article_page'),
]