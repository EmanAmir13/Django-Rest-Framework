from django import forms
from rest_framework import serializers
from students.models import Student


class StudentSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll_no = serializers.IntegerField()
    city = serializers.CharField(max_length=100)


    def create(self,validate_data):
        return Student.objects.create(**validate_data)


# class StudentForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     roll_no = forms.IntegerField()
#     city = forms.CharField(max_length=100)
