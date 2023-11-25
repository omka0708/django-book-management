from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from services.tasks import send_welcome_letter_task


class UserListAPI(generics.ListAPIView):
    # View for getting all users (GET)
    permission_classes = [
        permissions.IsAdminUser
    ]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetailAPI(generics.RetrieveAPIView):
    # View for getting specific user (GET)
    permission_classes = [
        permissions.IsAdminUser
    ]
    queryset = User
    serializer_class = UserSerializer


class CurrentUserDetailAPI(generics.RetrieveAPIView):
    # View for getting current user (GET)
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class RegisterAPI(generics.GenericAPIView):
    # View for user registration (POST)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        send_welcome_letter_task.delay(user.id)
        return Response({"user": UserSerializer(user, context=self.get_serializer_context()).data,
                         "token": AuthToken.objects.create(user)[1]})


class LoginAPI(generics.GenericAPIView):
    # View for user login (POST)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({"user": UserSerializer(user, context=self.get_serializer_context()).data,
                         "token": AuthToken.objects.create(user)[1]})
