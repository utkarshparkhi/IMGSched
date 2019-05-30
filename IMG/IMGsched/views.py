from django.shortcuts import render
from . import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
@api_view(['GET'])
def invited_events(request,a):
    if request.method == 'GET':
        invited_events = models.InvitedEvent.objects.filter(invitedUsers__id = a)
        serializer = serializers.InvitedEventSerializer(invited_events,many =True)
        return Response(serializer.data)    

@api_view(['GET'])
def general_events(request):
    if request.method == 'GET':
        events = models.GeneralEvent.objects.all()
        serializer = serializers.GeneralEventSerializer(events,many = True)
        return Response(serializer.data)