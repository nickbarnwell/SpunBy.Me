from django.db import models
from django.template.defaultfilters import slugify

import gdata.youtube, gdata.youtube.service
import pylast
import math, datetime


LASTFM_API_KEY = '522cc370a4cc1ee8029e065e08a168fb'
LASTFM_API_SECRET = 'b5115b3e49d6c1db271f73146d4ef413'
YOUTUBE_DEVELOPER_KEY = 'AI39si6AP91ntgKKeVQCWuRve6O-eLOunrtzdufBwlXX3HpiPg5HmrzX6M8G4iMwhBf6llht20idsxzpe9o_W41sRnBXXq7UcQ'

class User(models.Model):
  first_name = models.CharField(blank=False, max_length=255)
  last_name = models.CharField(blank=False, max_length=255)

class Song(models.Model):
  title = models.CharField(blank=False, max_length=255)
  artist = models.CharField(blank=False, max_length=255)
  video_id = models.CharField(blank=False, max_length=64)
  
  def __unicode__(self):
    return "%s - %s" % (self.title, self.artist)

  def search(self, query):
    network = pylast.LastFMNetwork(
      api_key=LASTFM_API_KEY, api_secret=LASTFM_API_SECRET)
    search = network.search_for_track('', query)
    tracks = search.get_next_page()
    return [dict(title=t.get_title(), artist=str(t.get_artist())) for t in tracks]
  
  def load_video_id(self):
    yt_service = gdata.youtube.service.YouTubeService()
    yt_service.developer_key = YOUTUBE_DEVELOPER_KEY
    query = gdata.youtube.service.YouTubeVideoQuery()
    query.vq = '%s - %s' % (self.artist, self.title)
    query.orderby = 'relevance'
    query.racy = 'include'
    feed = yt_service.YouTubeQuery(query)
    try:
      entry = iter(feed.entry).next()
      self.video_id = entry.id.text.split('/')[-1]
      return True
    except StopIteration:
      return False
  
  @classmethod
  def add_song(cls, artist, title):
    s = Song(title=title, artist=artist)
    res = Song.objects.filter(artist=artist, title=title)
    if res.count() == 0:
      if s.load_video_id():
        s.save()
      else:
        raise Exception
    else:
      s = res[0]
    return s

  def to_hash(self):
    return {'title':self.title, 'artist':self.artist, 'video_id':self.video_id}

class Party(models.Model):
  name = models.CharField(max_length=50, unique=True)
  created_at = models.DateTimeField(auto_now_add=True, blank=False)
  songs = models.ManyToManyField(Song, through='QueueData')
  slug = models.SlugField(editable=False)

  def __unicode__(self):
    return self.name

  def sorted_queue(self):
    return sorted(QueueData.objects.filter(party=self), key=lambda s: s.confidence)
  
  def pop(self):
    queue = sorted(QueueData.objects.filter(party=self), key=lambda s: s.confidence)
    if len(queue) > 0:
      s = qd.song
      qd.delete()
      return s
    else:
      return None

  @property
  def expired(self):
    return datetime.datetime.now() >= self.created_at+datetime.timedelta(24)

  def save(self, *args, **kwargs):
    if not self.id:
        self.slug = slugify(self.slug)
        super(Party, self).save(*args, **kwargs)


class QueueData(models.Model):
  song = models.ForeignKey(Song, blank=False)
  party = models.ForeignKey(Party, blank=False)
  added_at = models.DateTimeField(auto_now_add=True, blank=False)
  upvotes = models.IntegerField(default=1, blank=False)
  downvotes = models.IntegerField(default=0, blank=False)

  def to_hash(self):
    h = { 'votes': self.upvotes + self.downvotes }
    h.update(self.song.to_hash())
    return h

  def vote(self, vtype):
    if vtype == 'up':
      self.upvotes += 1
      votes = self.upvotes
    elif vtype == 'down':
      self.downvotes -= 1
      votes = self.upvotes

    return votes

  def find_by_party_song(pid, sid):
    objs = QueueData.objects.filter(song=Song.objects.get(pk=sid), party=Party.objects.get())
    if objs.count() != 0:
      return objs[0]

  def _confidence(self):
    n = self.upvotes + self.downvotes

    if n == 0:
      return 0

    z = 1.0
    phat = float(self.upvotes) / n
    return math.sqrt(phat+z*z/(2*n)-z*((phat*(1-phat)+z*z/(4*n))/n))/(1+z*z/n)
  
  @property
  def confidence(self):
    if self.upvotes - self.downvotes == 0:
      return 0
    else:
      return self._confidence(self)
  
  def __unicode__(self):
    return "Party: %s -- Song: %s" % (self.party, self.song)
