from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.request import Request
from django.core.cache import cache

from uuid import uuid4

from .models import CustomUser
from .serializers import UserSerializer
from .encryption import encrypt_user_id
from core.settings import TICKET_EXPIRE_TIME

class RegisterUser(generics.GenericAPIView):
    serializer_class = UserSerializer

    def get_permissions(self, *args, **kwargs):
        if self.request.method in ['GET']:
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.AllowAny()]

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
    
    def get(self, request:Request):
        ticket = str(uuid4())
        if request.user.is_anonymous:
            cache.set(ticket, False, TICKET_EXPIRE_TIME)
        else:
            ticket_value = encrypt_user_id(request.user.id)
            cache.set(ticket, ticket_value, TICKET_EXPIRE_TIME)

        return Response({'ticket': ticket}, status=status.HTTP_200_OK)



class UsersList(generics.ListAPIView):
    serializer_class = UserSerializer

    queryset = CustomUser.objects.all()

    permission_classes = (permissions.AllowAny,)
