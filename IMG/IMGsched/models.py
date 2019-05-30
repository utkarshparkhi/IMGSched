from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    email = models.EmailField(unique= True)
    password = models.CharField(max_length =(16))
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)



    

class GeneralEvent(models.Model):
        
    title = models.CharField(max_length = 30)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.CharField(max_length = 200,blank = True)
    time = models.DateTimeField()
    created_on = models.DateTimeField(default = timezone.now)
    location = models.CharField(max_length = 50)

class InvitedEvent(models.Model):
        
    title = models.CharField(max_length = 30)
    creator = models.ForeignKey(User,on_delete=models.PROTECT,related_name='Creator')
    description = models.CharField(max_length = 200,blank = True)
    time = models.DateTimeField()
    created_on = models.DateTimeField(default = timezone.now)
    location = models.CharField(max_length = 50)
    invitedUsers = models.ManyToManyField(User,related_name='usersinvited')
class comments(models.Model):
    content = models.CharField(max_length=(100))
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    Event = models.ForeignKey(GeneralEvent,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default = timezone.now)

