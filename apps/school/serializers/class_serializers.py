import django_filters
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from apps.school.models import Student, Class, Teacher, Mailing


class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = ("id", "title")
        

class ClassCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Class
        fields = ("id", "title", "teacher", "student")
        
        
class MailingCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Mailing
        fields = ("title", "description")
