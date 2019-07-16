from django.contrib.auth.models import User
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone
import asyncio
import json
from . import serializers
from .models import Gcomments,Icomments
import functools
import requests 


class CommentConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        
        
        e = self.scope['url_route']['kwargs']['event']
        i = self.scope['url_route']['kwargs']['event_id']
        if(e == 'generalevent'):
            print(i)
            self.chat_room = e+str(i)
        await self.channel_layer.group_add(
            self.chat_room,
            self.channel_name
        )
        await self.send({
            'type':'websocket.accept'
        })
        

    async def websocket_disconnect(self, event):
        print("disconnected",event)

    
    async def websocket_receive(self, event):
       
       print(json.loads(event['text']))
       data = json.loads(event['text'])
       message = data['message']
       headers = {"Authorization":"Bearer "+data['token']}
       
       loop = asyncio.get_event_loop()
       r = loop.run_in_executor(None,functools.partial(requests.get,"http://127.0.0.1:8000/authentication/getusername/",headers=headers))
       ans = await r
       ans = ans.json()
       
       user = User.objects.get(id=ans['id'])
      
      
       i = self.scope['url_route']['kwargs']['event_id']
       a = serializers.GCommentSerializer(data = {
           'user':user.id,
           'content':message,
           'gEvent':i,
           'pub_date':timezone.now()
       })
       a.is_valid()
       
       a.save()
       
       
       d = a.data
       d['user'] = user.username
       print(user.username)
       await self.channel_layer.group_send(
           self.chat_room,
           {
           'type':'chat_message',
           'text':json.dumps(d)
       }
       )
       
       print("recieve",event)

    
    async def chat_message(self,event):
        await self.send({
            "type":"websocket.send",
            "text":event["text"]
        })


    