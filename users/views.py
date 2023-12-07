from rest_framework import generics, permissions, status
from rest_framework.response import Response
# from dj_rest_auth.registration.views import RegisterView
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import IntegrityError

from .models import CustomUser
from .serializers import UserSerializer

class RegisterUser(generics.CreateAPIView):
    serializer_class = UserSerializer

    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = self.perform_create(serializer)
        except IntegrityError as e:
            return Response({'error': 'Email or username is already in use.'}, status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        return Response({'access_token': access_token, 'refresh': refresh_token, 'message': 'User successfully registered'}, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        user = serializer.save()

        return user

class UsersList(generics.ListAPIView):
    serializer_class = UserSerializer

    queryset = CustomUser.objects.all()

    permission_classes = (permissions.AllowAny,)
