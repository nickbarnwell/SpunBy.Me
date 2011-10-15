from django.db import models
# Create your models here.

class User(models.Model):
  first_name = models.CharField(blank=False, max_length=255)
  last_name = models.CharField(blank=False, max_length=255)

class Song(models.Model):
  title = models.CharField(blank=False, max_length=255)
  artist = models.CharField(blank=False, max_length=255)
  swf_url = models.URLField(blank=False)
  
  def __unicode__(self):
    return "%s - %s" % (self.title, self.artist)

class Party(models.Model):
  name = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True, blank=False)
  songs = models.ManyToManyField(Song, through='QueueData')

  @property
  def expired(self):
    return datetime.datetime.now() >= self.created_at+datetime.timedelta(24)

class QueueData(models.Model):
  song = models.ForeignKey(Song, blank=False)
  party = models.ForeignKey(Party, blank=False)
  added_at = models.DateTimeField(auto_now_add=True, blank=False)
  upvotes = models.IntegerField(default=1, blank=False)
  downvotes = models.IntegerField(default=1, blank=False)
