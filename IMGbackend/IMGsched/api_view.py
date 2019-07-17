from django.shortcuts import render
from . import models
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.db.models import Q

import requests




@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def invited_events_home(request):
    if request.method == 'GET':
        a = request.user
        invited_eventsc = models.InvitedEvent.objects.filter(Q(creator = a) , time__gte=timezone.now())
        invited_eventsi = models.InvitedEvent.objects.filter(Q(invitedUsers = a) , time__gte=timezone.now())
        invited_events = []
        for i in invited_eventsc:
                if i not in invited_eventsi:
                        
                        invited_events.append(i)
        for i in invited_eventsi:
                invited_events.append(i)
        
        serializer = serializers.InvitedEventSerializer(invited_events,many =True)
        for e in serializer.data:
                        u = User.objects.get(id = e['creator'])
                        e['username'] = u.username
                        U = []
                        e['name'] = 'invitedevent'
                        for i in e['invitedUsers']:
                                u = User.objects.get(id = i)
                                U.append(u.username)
                        e['invitedUsers'] = U
        return Response(serializer.data)    
    elif request.method == 'PUT':
        request.data['creator'] = request.user.id
        a = serializers.InvitedEventSerializer(data = request.data)
        if a.is_valid():
                a.save()        
                return Response(a.data)

        
        return Response(a.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def general_events_home(request):
        if request.method == 'GET':
                events = models.GeneralEvent.objects.filter(time__gte=timezone.now())
                serializer = serializers.GeneralEventSerializer(events,many = True)
                for e in serializer.data:
                        u = User.objects.get(id = e['creator'])
                        e['username'] = u.username
                        e['invitedUsers'] = ['all']
                        e['name'] = 'generalevent'
                return Response(serializer.data)
        elif request.method == 'PUT':
                request.data['creator'] = request.user.id
                print(request.data['creator'])
                event = serializers.GeneralEventSerializer(data = request.data)
                if event.is_valid():
                        event.save()
                        return Response(event.data)
                return Response(event.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def general_events_detail(request,event_id):
        if request.method == 'GET':
                event = models.GeneralEvent.objects.get(id = event_id)
                serializer = serializers.GeneralEventSerializer(event)
                e = serializer.data
                e['invitedUsers'] = ['all']
                return Response(e)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def invite_users(request,event_id):
        if request.method == 'POST':
                event = models.InvitedEvent.objects.get(id=event_id)
                ser = serializers.InvitedEventSerializer(event)
                if request.user == event.creator:
                        a = request.POST.get('ids',[])        
                        for i in a:
                                user = models.User.objects.get(id = i)
                                user.save()
                                event.save()
                                event.invitedUsers.add(user)
                                user.save()
                                event.save()
                        return Response(ser.data)
                return Response("you have no right")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def invited_event_details(request,invited_event_id):
        if request.method == 'GET':
                event = models.InvitedEvent.objects.get(id=invited_event_id)
                if (request.user in event.invitedUsers.all()) or request.user == event.creator:
                        event_s = serializers.InvitedEventSerializer(event)
                        event_S = event_s.data
                        a = []
                        for i in event_S['invitedUsers']:
                                u = User.objects.get(id = i)
                                a.append(u.username)
                        event_S['invitedUsers'] = a
                        u = User.objects.get(id = event_S['creator'])
                        event_S['creator'] = u.username
                        return Response(event_S)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def invited_event_comment(request,invited_event_id):
        if request.method == 'GET':
                comments = models.Icomments.objects.filter(iEvent__id = invited_event_id)
                comments_s = serializers.ICommentSerializer(comments,many = True)
                event = models.InvitedEvent.objects.get(id=invited_event_id)

                if (request.user in event.invitedUsers.all()) or request.user == event.creator:
                        for c in comments_s.data:
                                U = User.objects.get(id=c['user'])
                                c['user'] = U.username
                        return Response(comments_s.data)
                else:
                        return Response('you are not invited to this event')



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def general_event_comment(request,event_id):
        if request.method == 'GET':
                comments = models.Gcomments.objects.filter(gEvent__id = event_id)

                comments_s = serializers.GCommentSerializer(comments,many = True)
                for c in comments_s.data:
                        U = User.objects.get(id=c['user'])
                        c['user'] = U.username
                
                
                
                return Response(comments_s.data)
                        

                


