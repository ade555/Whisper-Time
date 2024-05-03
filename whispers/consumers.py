from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from django.core.cache import cache
from asgiref.sync import sync_to_async
from urllib.parse import parse_qsl

import json

from .models import Conversation, Message
from .serializers import MessageSerializer

from users.encryption import decrypt_user_id

User = get_user_model()


class MessageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        try:
            query_string = self.scope['query_string'].decode('utf-8')
            query_params = dict(parse_qsl(query_string))
            ticket = query_params.get('ticket')
            user_id = cache.get(ticket)
            if user_id is not None:
                try:
                    decrypted_user_id = decrypt_user_id(user_id)
                    user = await sync_to_async(User.objects.get)(id=decrypted_user_id)
                except User.DoesNotExist:
                    user = None

            if not cache.delete(ticket):
                raise Exception('ticket not found')
            
            if user is None or user_id ==False:
                await self.close(403)
            else:
                self.user = user

        except Exception as e:
            print(str(e))
            await self.close(403)
            return
        
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_txt = text_data_json["message"]
        message_sender = self.user
        conversation = await sync_to_async(Conversation.objects.get)(id=int(self.room_name))
        message = await sync_to_async(Message.objects.create)(sender=message_sender, msg_text=message_txt, related_conversation=conversation)
        serializer = MessageSerializer(instance=message)

        await self.channel_layer.group_send(self.room_group_name, {"type":"chat_message", "message":dict(serializer.data)})
    
    async def chat_message(self, event):
       data = event.copy()
       data.pop("type")
       await self.send(text_data=json.dumps(data))