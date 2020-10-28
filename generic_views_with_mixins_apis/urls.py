from django.urls import path
from .views import ArticleGenericApiView

urlpatterns = [
    path('articles/<int:id>/', ArticleGenericApiView.as_view())
    # path('articles/', ArticleGenericApiView.as_view())
]
