from django.contrib import admin
from django.urls import path, include
from .views import article_list, article_detail

urlpatterns = [
    path('articles/', article_list),
    path('article-detail/<int:pk>/', article_detail, name='article_detail')
]
