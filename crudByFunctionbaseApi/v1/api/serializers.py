from rest_framework import serializers
from api.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'roll_no', 'city']