from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.school.models import Student
from apps.school.tasks import send_message_email

from apps.school.serializers.class_serializers import (
    ClassCreateSerializer,
)


class ClassCreateView(APIView):
    serializer_class = ClassCreateSerializer
    # permission_classes = (IsAuthenticated,)

    def post(self, request): # noqa
        serializer = ClassCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
