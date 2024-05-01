from django.urls import re_path

from .consumers import MessageConsumer

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\d+)/$", MessageConsumer.as_asgi(), name="chat_socket"),
]