from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/v1/student-info/<int:pk>', student_details, name='student_details'),
    path('api/v1/student-info/', students_list, name='students_list'),
    path('api/v1/student-create/', student_create, name='student_create'),
]
