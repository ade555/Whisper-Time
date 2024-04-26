from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.request import Request

from django.db.models import Q
from django.contrib.auth import get_user_model

from .serializers import MessageSerializer, ConversationSerializer, ListConversationSerializer
from .models import Conversation

User = get_user_model()

class ListCreateConversation(generics.GenericAPIView):
    serializer_class = ConversationSerializer

    def post(self, request:Request):
        data = request.data