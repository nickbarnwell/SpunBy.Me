from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import gdata.youtube
import gdata.youtube.service
import pylast
import cjson

LASTFM_API_KEY = '522cc370a4cc1ee8029e065e08a168fb'
LASTFM_API_SECRET = 'b5115b3e49d6c1db271f73146d4ef413'
YOUTUBE_DEVELOPER_KEY = 'AI39si6AP91ntgKKeVQCWuRve6O-eLOunrtzdufBwlXX3HpiPg5HmrzX6M8G4iMwhBf6llht20idsxzpe9o_W41sRnBXXq7UcQ'

def search(request):
  network = pylast.LastFMNetwork(
    api_key=LASTFM_API_KEY, api_secret=LASTFM_API_SECRET)
  search = network.search_for_track('', request.GET.get('q'))
  tracks = search.get_next_page()
  result = [dict(title=t.get_title(), artist=str(t.get_artist())) for t in tracks]
  return HttpResponse(cjson.encode(result), mimetype='application/json')

def get_swf_for_song(artist, title):
  yt_service = gdata.youtube.service.YouTubeService()
  yt_service.developer_key = YOUTUBE_DEVELOPER_KEY
  query = gdata.youtube.service.YouTubeVideoQuery()
  query.vq = '%s - %s' % (artist, title)
  query.orderby = 'relevance'
  query.racy = 'include'
  feed = yt_service.YouTubeQuery(query)
  entry = iter(feed.entry).next()
  return entry.GetSwfUrl()

def add_song(request):
  #party = get_object_or_404(Party, name=request.GET.get('party'))
  return HttpResponse(get_swf_for_song(request.GET.get('artist'), request.GET.get('title')))
