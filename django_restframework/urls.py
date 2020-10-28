from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('languages.urls')),
    path('function-based-api/', include('function_based_api.urls')),
    path('api-view-decorator/', include('api_view_decorator_based_apis.urls')),
    path('class-based-views/', include('class_based_views_apis.urls')),
    path('generic-views-with-mixins/',
         include('generic_views_with_mixins_apis.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
