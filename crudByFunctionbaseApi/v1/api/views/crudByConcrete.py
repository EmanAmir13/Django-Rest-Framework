from api.models.student import Student
from v1.api.serializers import StudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView


class StudentLC(ListAPIView, CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetriveUpdateDelete(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
