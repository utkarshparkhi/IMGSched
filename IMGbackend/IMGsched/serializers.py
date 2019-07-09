from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
class GeneralEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GeneralEvent
        fields = ('id','title','creator','description','time','created_on','location')
class InvitedEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvitedEvent
        fields = ('id','title','creator','description','time','created_on','location','invitedUsers')
    



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.comments
        fields = ( 'content','user','Event','pub_date')
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User    
        fields =('username','password')

