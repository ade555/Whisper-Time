from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
import json

from .models import Conversation, Message
from .serializers import MessageSerializer

User = get_user_model()


class MessageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self.channel_layer.group_send(self.room_group_name, {"type":"chat_message", "message":message})
    
    async def chat_message(self, event):
        message_txt = event["message"]
        conversation = Conversation.objects.get(id=int(self.room_name))
        message_sender = self.scope["user"]
        message = Message.objects.create(sender=message_sender, msg_text=message_txt, related_conversation=conversation)
        serializer = MessageSerializer(instance=message)

        self.send(text_data=json.dumps({"message":serializer.data}))