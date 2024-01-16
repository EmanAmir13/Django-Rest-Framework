from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from v1.api.auth import CustomAuthToken

router = DefaultRouter()

router.register('studentapi', StudentModelViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('gettoken/', CustomAuthToken.as_view())
]
