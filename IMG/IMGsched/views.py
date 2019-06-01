from django.shortcuts import render
from . import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from django.utils import timezone
@api_view(['GET','PUT'])
def invited_events_home(request,a):
    if request.method == 'GET':
        invited_events = models.InvitedEvent.objects.filter(invitedUsers__id = a , time__gte=timezone.now())
        serializer = serializers.InvitedEventSerializer(invited_events,many =True)
        return Response(serializer.data)    
    elif request.method == 'PUT':
        a = serializers.InvitedEventSerializer(data = request.data)
        if a.is_valid():
                a.save()
                return Response(a.data)

        
        return Response(a.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def general_events_home(request):
        if request.method == 'GET':
                events = models.GeneralEvent.objects.all()
                serializer = serializers.GeneralEventSerializer(events,many = True)
                return Response(serializer.data)
        elif request.method == 'PUT':
                event = serializers.GeneralEventSerializer(data = request.data)
                if event.is_valid():
                        event.save()
                        return Response(event.data)
                return Response(event.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def invite_users(request,id,event_id):
        if request.method == 'PUT':
                event = models.InvitedEvent.objects.get(id=event_id)
                ser = serializers.InvitedEventSerializer(event)
                if models.User.objects.get(id = id) == event.creator:        
                        for i in request.data['ids']:
                                user = models.User.objects.get(id = i)
                                user.save()
                                event.save()
                                event.invitedUsers.add(user)
                                user.save()
                                event.save()
                        return Response(ser.data)
                return Response("you have no right")

                         
                


