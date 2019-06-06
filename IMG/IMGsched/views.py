from django.shortcuts import render
from . import models
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from django.utils import timezone
from rest_framework.permissions import AllowAny,IsAuthenticated

from django.db.models import Q

import requests




@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def invited_events_home(request):
    if request.method == 'GET':
        a = request.user['id']
        invited_events = models.InvitedEvent.objects.filter(Q(invitedUsers__id = a)|Q(creator__id = a) , time__gte=timezone.now())
        
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
@permission_classes([IsAuthenticated])
def invite_users(request,event_id):
        if request.method == 'PUT':
                event = models.InvitedEvent.objects.get(id=event_id)
                ser = serializers.InvitedEventSerializer(event)
                if request.user == event.creator:        
                        for i in request.data['ids']:
                                user = models.User.objects.get(id = i)
                                user.save()
                                event.save()
                                event.invitedUsers.add(user)
                                user.save()
                                event.save()
                        return Response(ser.data)
                return Response("you have no right")

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def invited_event_details(request):
        if request.method == 'POST':
                event = models.InvitedEvent.objects.get(id=request.data['id'])
                if (request.user in event.invitedUsers.all()) or request.user == event.creator:
                        event_s = serializers.InvitedEventSerializer(event)
                        a = serializers.UserSerializer(request.user)
                        return Response(a.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def invited_event_comment(request,invited_event_id):
        if request.method == 'GET':
                comments = models.comments.objects.filter(Event__id == invited_event_id)
                comments_s = serializers.CommentSerializer(comments,many = True)
                return Response(comments_s.data)
        
                


