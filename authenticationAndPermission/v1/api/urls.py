from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from v1.api.auth import CustomAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()

router.register('studentapi', StudentModelViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('gettoken/', CustomAuthToken.as_view())
    path('gettoken/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refresh-token/', TokenVerifyView.as_view(),name='token_refresh'),
    path('verify-token/', TokenRefreshView.as_view(),name='token_verify'),

]
