from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.school.models import Student
from apps.school.tasks import send_mailing

from apps.school.serializers.class_serializers import (
    ClassCreateSerializer,
    MailingCreateSerializer,
)


class ClassCreateView(APIView):
    serializer_class = ClassCreateSerializer

    def post(self, request): # noqa
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MailingCreateView(APIView):
    serializer_class = MailingCreateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        title = validated_data.get("title")
        description = validated_data.get("description")
        serializer.save()
        send_mailing.delay(title, description)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
