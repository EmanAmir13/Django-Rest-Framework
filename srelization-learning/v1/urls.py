from django.urls import path, include

from v1.students import urls as student_urls

urlpatterns = [
    path('', include(student_urls)),
]