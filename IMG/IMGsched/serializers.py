from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
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
    
class CreateUserSerializer(serializers.ModelSerializer):
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    class Meta:
        model = User
        fields = ( 'username','email','password','first_name','last_name')
        extra_kwargs = {
            'password': {'write_only': True}
        }


