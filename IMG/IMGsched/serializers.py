from rest_framework import serializers
from . import models
class GeneralEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GeneralEvent
        fields = ('title','creator','description','time','created_on','location')
class InvitedEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvitedEvent
        fields = ('title','creator','description','time','created_on','location','invitedUsers')
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.comments
        fields = ( 'content','user','Event','pub_date')
      
