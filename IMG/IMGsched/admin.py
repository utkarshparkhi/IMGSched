from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.GeneralEvent)
admin.site.register(models.InvitedEvent)
admin.site.register(models.comments)