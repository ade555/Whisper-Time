from rest_framework import serializers
from .models import Message, Conversation
from users.serializers import UserSerializer

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ['related_conversation']


class ConversationSerializer(serializers.ModelSerializer):
    convo_starter = UserSerializer()
    convo_receiver = UserSerializer()
    messages = MessageSerializer(many=True)
    
    class Meta:
        model = Conversation
        fields = ["convo_starter", "convo_receiver", "messages"]


class ListConversationSerializer(serializers.ModelSerializer):
    convo_starter = UserSerializer()
    convo_receiver = UserSerializer()
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = "__all__"

    def get_last_message(self, instance):
        last_msg = instance.messages.first()
        print(last_msg)
        return MessageSerializer(instance=last_msg).data