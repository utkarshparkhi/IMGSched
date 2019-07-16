from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.




    

class GeneralEvent(models.Model):
    
    title = models.CharField(max_length = 30)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.CharField(max_length = 200,blank = True)
    time = models.DateTimeField()
    created_on = models.DateTimeField(default = timezone.now)
    location = models.CharField(max_length = 50)
    class Meta:
        ordering = ('time','title')

class InvitedEvent(models.Model):
        
    title = models.CharField(max_length = 30)
    creator = models.ForeignKey(User,on_delete=models.PROTECT,related_name='Creator')
    description = models.CharField(max_length = 200,blank = True)
    time = models.DateTimeField()
    created_on = models.DateTimeField(default = timezone.now)
    location = models.CharField(max_length = 50)
    invitedUsers = models.ManyToManyField(User,related_name='usersinvited')
    class Meta:
        ordering = ('time','title')



class Gcomments(models.Model):

    
    content = models.CharField(max_length=(100))
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    gEvent = models.ForeignKey(GeneralEvent,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default = timezone.now)
    class Meta:
        ordering = ['pub_date']

class Icomments(models.Model):
    content = models.CharField(max_length=(100))
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    iEvent = models.ForeignKey(InvitedEvent,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default = timezone.now)
    class Meta:
        ordering = ['pub_date']
