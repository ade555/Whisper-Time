from django.urls import path
from .views import ListCreateConversation, ListAllConversations, get_conversation

urlpatterns = [
    path("", ListAllConversations.as_view()),
    path("start/", ListCreateConversation.as_view()),
    path('<int:id>/', get_conversation, name='get_conversation'),
]
