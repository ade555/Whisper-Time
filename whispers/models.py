from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Conversation(models.Model):
    convo_starter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="convo_initiator")
    convo_receiver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="convo_receipent")
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="msg_sender")
    msg_text = models.TextField()
    related_conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-sent_at"]

