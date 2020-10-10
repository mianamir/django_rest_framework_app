from django.urls import path, include
from .views import LanguageViewSet
from rest_framework import routers

router =  routers.DefaultRouter()
router.register('lanaguages', LanguageViewSet)

urlpatterns = [
    path('', include(router.urls))
]
