from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path

from websocketTest import consumer

ws_urlPatterns = [
    path('ws/data/',consumer.Dashboard.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(URLRouter(ws_urlPatterns))

})