from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import IntegrityError

from .models import CustomUser
from .serializers import UserSerializer

class RegisterUser(generics.CreateAPIView):
    serializer_class = UserSerializer

    permission_classes = (permissions.AllowAny,)

    def post(self, request:Request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message":"successful",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        response = {
            "message":"failed",
            "info": serializer.errors
        }
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

class UsersList(generics.ListAPIView):
    serializer_class = UserSerializer

    queryset = CustomUser.objects.all()

    permission_classes = (permissions.AllowAny,)
