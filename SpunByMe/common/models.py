from django.db import models
# Create your models here.
class Song(models.Model):
  title = models.CharField(blank=False, max_length=255)
  artist = models.CharField(blank=False, max_length=255)
  swf_url = models.URLField(blank=False)
  
  def __unicode__(self):
    return "%s - %s" % (self.title, self.artist)

class SongQueue(models.Model):
  songs = models.ManyToManyField(Song, through='QueueData')

class QueueData(models.Model):
  song = models.ForeignKey(Song, blank=False)
  queue = models.ForeignKey(SongQueue, blank=False)
  added_at = models.DateTimeField(auto_now_add=True, blank=False)
  upvotes = models.IntegerField(default=1, blank=False)
  downvotes = models.IntegerField(default=1, blank=False)
