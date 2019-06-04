from django.shortcuts import render
from . import models
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from django.utils import timezone
from rest_framework.permissions import AllowAny
from .serializers import CreateUserSerializer
from django.db.models import Q

import requests

CLIENT_ID = 'CgZ1K9yegmJRtTNf1JONio0yK1aqj4ZHR2Dg81gX'
CLIENT_SECRET = '173EkmYE87gNqB8bLrqp84MHIkYjgZB3xsrKwAPaZbwgOTgzA4PfN6t7wGZFAg8sqmmznkawxaBQXCAxFvjIvUzcSRW3bJotVOVCCHOfKPAl87wwS47ySyJtdXdGHW1m'
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
        '''
        Registers user to the server. Input should be in the format:
        {"username": "username", "password": "1234abcd","first_name":"first","last_name":"last"}
        '''
        # Put the data from the request into the serializer 
        serializer = CreateUserSerializer(data=req/uest.data) 
        # Validate the data
        if serializer.is_valid():
                # If it is valid, save the data (creates a user).
                serializer.save() 
                # Then we get a token for the created user.
                # This could be done differentley 
                d = request.data
                d['client_id'] = CLIENT_ID
                d['client_secret'] = CLIENT_SECRET
                d['grant_type'] = 'password'
                r = requests.post('http://127.0.0.1:8000/o/token/', 
                        data=d
                )
                return Response(r.json())
        return Response(serializer.errors)



@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    
        d = request.data
        d['client_id'] = CLIENT_ID
        d['client_secret'] = CLIENT_SECRET
        d['grant_type'] = 'password'
        
        r = requests.post('http://127.0.0.1:8000/o/token/', 
                data=d,
        )
        return Response(r.json())



@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    '''
    Registers user to the server. Input should be in the format:
    {"refresh_token": "<token>"}
    '''
    r = requests.post(
    'http://127.0.0.1:8000/o/token/', 
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    '''
    Method to revoke tokens.
    {"token": "<token>"}
    '''
    r = requests.post(
        'http://127.0.0.:8000/o/revoke_token/', 
        data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    # If it goes well return sucess message (would be empty otherwise) 
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    # Return the error if it goes badly
    return Response(r.json(), r.status_code)



@api_view(['GET','PUT'])
def invited_events_home(request,a):
    if request.method == 'GET':
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

@api_view(['GET'])
def invited_event_details(request,id,invited_event_id):
        if request.method == 'GET':
                event = models.InvitedEvent.objects.get(id = invited_event_id)
                
                event_s = serializers.InvitedEventSerializer(event)
                return Response(event_s.data)

@api_view(['GET'])
def invited_event_comment(request,invited_event_id):
        if request.method == 'GET':
                comments = models.comments.objects.filter(Event__id == invited_event_id)
                comments_s = serializers.CommentSerializer(comments,many = True)
                return Response(comments_s.data)
        
                


