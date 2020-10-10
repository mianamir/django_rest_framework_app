from django.urls import path, include
from .views import (ParadigmViewSet, 
                    LanguageViewSet, 
                    ProgrammerViewSet)
from rest_framework import routers

router =  routers.DefaultRouter()
router.register('paradigms', ParadigmViewSet)
router.register('lanaguages', LanguageViewSet)
router.register('programmers', ProgrammerViewSet)

urlpatterns = [
    path('', include(router.urls))
]
