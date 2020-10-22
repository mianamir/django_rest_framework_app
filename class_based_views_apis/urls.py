from django.urls import path
from .views import ArticleApiView, ArticleDetailApiView

urlpatterns = [
    path('articles/', ArticleApiView.as_view()),
    path('article-detail/<int:pk>/', ArticleDetailApiView.as_view())
]
