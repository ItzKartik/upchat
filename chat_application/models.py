from __future__ import unicode_literals
from django.db import models
import uuid
from django.contrib.auth.models import User

class group(models.Model):
    model_id = models.UUIDField(default=uuid.uuid4)
    user1 = models.CharField(max_length=100)
    user2 = models.CharField(max_length=100)

class chats(models.Model):
    link = models.ForeignKey(group, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    message = models.CharField(max_length=2000, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

class files(models.Model):
    link = models.ForeignKey(group, on_delete=models.CharField)
    file_field = models.FileField(upload_to='')
    created_on = models.DateTimeField(auto_now_add=True)