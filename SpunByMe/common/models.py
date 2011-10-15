from django.db import models
# Create your models here.

import gdata.youtube
import gdata.youtube.service
import pylast

LASTFM_API_KEY = '522cc370a4cc1ee8029e065e08a168fb'
LASTFM_API_SECRET = 'b5115b3e49d6c1db271f73146d4ef413'
YOUTUBE_DEVELOPER_KEY = 'AI39si6AP91ntgKKeVQCWuRve6O-eLOunrtzdufBwlXX3HpiPg5HmrzX6M8G4iMwhBf6llht20idsxzpe9o_W41sRnBXXq7UcQ'


class Song(models.Model):
  title = models.CharField(blank=False, max_length=255)
  artist = models.CharField(blank=False, max_length=255)
  swf_url = models.URLField(blank=False)
  
  def __unicode__(self):
    return "%s - %s" % (self.title, self.artist)

  def search(self, query):
    network = pylast.LastFMNetwork(
      api_key=LASTFM_API_KEY, api_secret=LASTFM_API_SECRET)
    search = network.search_for_track('', query)
    tracks = search.get_next_page()
    return [dict(title=t.get_title(), artist=str(t.get_artist())) for t in tracks]
  
  def get_swf_for_song(self):
    yt_service = gdata.youtube.service.YouTubeService()
    yt_service.developer_key = YOUTUBE_DEVELOPER_KEY
    query = gdata.youtube.service.YouTubeVideoQuery()
    query.vq = '%s - %s' % (self.artist, self.title)
    query.orderby = 'relevance'
    query.racy = 'include'
    feed = yt_service.YouTubeQuery(query)
    entry = iter(feed.entry).next()
    self.swf_url = entry.GetSwfUrl()
    return self.swf_url != None
  
  def add_song(self, artist, title):
    s = Song(title=title, artist=artist)
    if Song.objects.filter(artist=s.artist, title=s.title).count() == 0:
      if s.get_swf_for_song():
        s.save()
      else:
        raise Exception
    else:
      s = Song.objects.filter(artist=artist, title=title)[0]
    return s

  def to_hash(self):
    return {'title':self.title, 'artist':self.artist, 'url':self.swf_url}

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