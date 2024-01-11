from django.urls import path, include

from v1.api import urls as student_urls

urlpatterns = [
    path('', include(student_urls)),
]