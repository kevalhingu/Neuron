from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Submission(models.Model):

    target_user = models.ForeignKey(User, on_delete=models.PROTECT)
    angry = models.FloatField(default=0.0)
    fear = models.FloatField(default=0.0)
    happy = models.FloatField(default=0.0)
    sad = models.FloatField(default=0.0)
    surprise = models.FloatField(default=0.0)

    at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-at']

class Doctor(models.Model):

    photo = models.ImageField(upload_to='media/image/', null=True)
    portfolio = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=15)

class Story(models.Model):
    image = models.ImageField(upload_to='media/image/', null=True)
    topic = models.CharField(max_length=50)
    primary = models.CharField(max_length=35)
    paragraph = models.TextField()
    range = models.JSONField(default=dict) # {"happy": [0.2, 0.4]}

class Game(models.Model):
    redirect_url = models.URLField()
    cover = models.URLField()
    badge = models.URLField()
    avatar = models.URLField()
    range = models.JSONField(default=dict) # {happy: [0.2, 0.4]}

class Therapy(models.Model):

    group = models.CharField(max_length=30) # speech|music|song
    url = models.FileField(upload_to='media/audio/', null=True)
    primary = models.CharField(max_length=60)
    range = models.JSONField(default=dict) # {happy: [0.2, 0.4]}


    