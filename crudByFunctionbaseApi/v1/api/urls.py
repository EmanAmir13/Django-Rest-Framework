from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('studentapi', StudentModelViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
    # path('api/v1/student-api/', StudentLC.as_view(), name='student_api'),
    # path('api/v1/student-api/', StudentCreate.as_view(), name='student_api'),
    # path('api/v1/student-api/<int:pk>/', StudentRetrive.as_view(), name='student_api'),
    # path('api/v1/student-api/<int:pk>/', StudentDestroy.as_view(), name='student_api'),
    # path('api/v1/student-api/<int:pk>/', StudentRetriveUpdateDelete.as_view(), name='student_api'),
    # path('api/v1/student-api/', StudentAPI.as_view(), name='student_api'),
    # path('api/v1/student-api/<int:pk>/', StudentAPI.as_view(), name='student_api'),
]
