from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack

import IMGsched.routing as IMGR
from django.conf.urls import url
application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(
            IMGR.websocket_urlpatterns
        )
    )
})