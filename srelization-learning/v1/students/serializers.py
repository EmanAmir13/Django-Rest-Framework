from django import forms
from rest_framework import serializers
from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)

    class Meta:
        model = Student
        fields = ['name', 'roll_no', 'city']

        extra_kwargs = {'name': {'read_only': True}}

# def start_with_e(value):
#     if value[0] != 'e':
#         raise serializers.ValidationError("Name should be start with E")
#     return value
#
#
# class StudentSerializer(serializers.Serializer):
#     # id = serializers.IntegerField()
#     # name = serializers.CharField(max_length=100, validators=[start_with_e])
#     name = serializers.CharField(max_length=100)
#     roll_no = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)
#
#     def create(self, validate_data):
#         return Student.objects.create(**validate_data)
#
#     def update(self, instance, validated_data):
#         print(instance.name)
#         instance.name = validated_data.get('name', instance.name)
#         print(instance.name)
#         instance.roll_no = validated_data.get('roll_no', instance.roll_no)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance
#
#     def validate_roll_no(self, value):
#         if value >= 200:
#             raise serializers.ValidationError('Seat Full')
#         return value
#
#     def validate(self, data):
#         nm = data.get('name')
#         ct = data.get('city')
#         if nm.lower() == 'mahi' and ct.lower() != 'Lahore':
#             raise serializers.ValidationError('City must be Lahore')
#         return data

# class StudentForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     roll_no = forms.IntegerField()
#     city = forms.CharField(max_length=100)
