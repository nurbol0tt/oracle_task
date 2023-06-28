import django_filters
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .class_serializers import ClassSerializer

from apps.school.models import Student, Class, Teacher


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"


class StudentListSerializer(serializers.ModelSerializer):
    classroom = ClassSerializer()

    class Meta:
        model = Student
        fields = ("id", "fio", "email", "classroom")


class StudentSearch(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='fio')

    class Meta:
        model = Student
        fields = ('fio',)


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ("number_phone", "password")

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return Teacher.objects.create(**validated_data)
