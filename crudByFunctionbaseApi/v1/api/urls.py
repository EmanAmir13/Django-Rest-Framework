from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/v1/student-api/', student_api, name='student_api'),
]
