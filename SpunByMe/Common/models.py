from django.db import models
from party.models import Party
# Create your models here.
class Song(models.Model):
 title = models.CharField(blank=False)
 artist = models.CharField(blank=False)
 swf_url = models.CharField(blank=False)

class SongQueue(models.Model):
  songs = models.ManyToManyField(Song, through='QueueData')
class QueueData(models.Model):
  song = models.ForeignKey(Song, blank=False)
  added_at = models.DateTimeField(auto_now_add=True, blank=False)
  upvotes = models.IntegerField(default=1, blank=False)
  downvotes = models.IntegerField(default=1, blank=False)
