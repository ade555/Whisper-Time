from django.urls import path
from .views import ListCreateConversation, ListAllConversations

urlpatterns = [
    path("", ListAllConversations.as_view()),
    path("start/", ListCreateConversation.as_view()),
]
