from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.school.models import Student
from apps.school.tasks import send_message_email
from apps.school.student_serializers import (
    StudentSerializer,
    StudentListSerializer,
    StudentSearch,
)


class StudentCreateView(APIView):
    serializer_class = StudentSerializer
    # permission_classes = (IsAuthenticated,)

    def post(self, request): # noqa
        email = request.data.get('email')
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        send_message_email.apply_async(args=[email], countdown=0)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StudentListView(APIView):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StudentSearch # noqa

    def get(self, request, *args, **kwargs):
        # /api/v1/student/list/?fio=fio
        queryset = Student.objects.all()
        filtered_queryset = self.filterset_class(request.GET, queryset=queryset).qs
        serializer = StudentListSerializer(filtered_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs): # noqa
        student = get_object_or_404(Student, id=kwargs["id"])
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentPatchView(APIView):
    permission_classes = (IsAuthenticated,)

    def patch(self, request, *args, **kwargs): # noqa
        student = get_object_or_404(Student, id=kwargs["id"])
        serializer = StudentSerializer(student, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class StudentDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs): # noqa
        student = get_object_or_404(Student, id=kwargs["id"])
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
