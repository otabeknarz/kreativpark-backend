from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("ws/seat/", consumers.SeatConsumer.as_asgi()),
]
