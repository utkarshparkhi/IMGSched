from django.conf.urls import url
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('IMGsched/<str:event>/<int:event_id>',consumers.CommentConsumer)
]