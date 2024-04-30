from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.request import Request

from django.db.models import Q
from django.contrib.auth import get_user_model

from .serializers import MessageSerializer, ConversationSerializer, ListConversationSerializer
from .models import Conversation

import logging
import traceback
import datetime

logger = logging.getLogger(__name__)

User = get_user_model()

class ListCreateConversation(generics.GenericAPIView):
    serializer_class = ConversationSerializer

    def post(self, request:Request):
        data = request.data
        username = data['username']
        try:
            convo_participant=User.objects.get(username=username)
            conversation = Conversation.objects.filter(Q(convo_starter=request.user, convo_receiver=convo_participant) | Q(convo_starter=convo_participant, convo_receiver=request.user))
            serializer = self.serializer_class(instance=conversation[0])
            if not conversation.exists():
                conversation = Conversation.objects.create(convo_starter=request.user, convo_receiver=convo_participant)
                serializer = self.serializer_class(instance=conversation)
            response = {
                "message":"success",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={"error":"user not found"}, status=status.HTTP_404_NOT_FOUND)
        # log any other exception
        except Exception as e:
            exception = {
                "error":str(e),
                "timestamp": datetime.datetime.now().isoformat(),
                "stack_trace": traceback.format_exc()
            }
            logger.error(f"\n{exception}")
            return Response(data={"error":"Unexpected error. Try again"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ListAllConversations(generics.GenericAPIView):
    def get(self, request:Request):
        conversations = Conversation.objects.filter(Q(convo_starter=request.user) | Q(convo_receiver=request.user))
        serializer = ListConversationSerializer(instance=conversations, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)