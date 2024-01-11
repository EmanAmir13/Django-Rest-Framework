from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/v1/student-api/', StudentAPI.as_view(), name='student_api'),
    path('api/v1/student-api/<int:pk>/', StudentAPI.as_view(), name='student_api'),
]
