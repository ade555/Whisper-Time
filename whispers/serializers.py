from rest_framework import serializers
from .models import Message, Conversation
from users.serializers import UserSerializer

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ['related_conversation']


class ConversationSerializer(serializers.ModelSerializerd):
    convo_starter = UserSerializer()
    conver_receiver = UserSerializer()
    messages = MessageSerializer(many=True)
    class Meta:
        model = Conversation
        fields = ["__all__"]


class ListConversationSerializer(serializers.ModelSerializer):
    convo_starter = UserSerializer()
    conver_receiver = UserSerializer()
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['convo_starter', 'convo_receiver', 'last_message']

    def get_last_message(self, instance):
        last_msg = instance.messages.first()
        return MessageSerializer(last_msg)