from api.models.student import Student
from v1.api.serializers import StudentSerializer
from rest_framework import viewsets


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
