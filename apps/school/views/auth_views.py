from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.school.serializers.student_serializers import RegisterSerializer


class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request, format=None): # noqa
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    pass
