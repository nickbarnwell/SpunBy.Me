from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from common.models import * 
import cjson
import urllib


def search(request):
  q = request.GET.get('q')
  result = Song().search('%s' % q)
  return HttpResponse(cjson.encode(result), mimetype='application/json')

def add_song(request, pid):
  artist = request.GET.get('artist')
  title = request.GET.get('title')
  party = Party.objects.get(pk=pid)

  s = Song.add_song(artist, title)
  QueueData(party=party, song=s).save()
  result = cjson.encode(s.to_hash())
  return redirect(party.viewer_url)
  
def vote(request):
  party_id = int(request.GET.get('party_id'))
  song_id = int(request.GET.get('song_id'))
  vtype = request.GET.get('type')
  qd = QueueData().find_by_party_song(party_id, song_id)
  qd.vote(vtype)
  qd.save()
  return HttpResponse('{votes:%d}' % qd.votes, mimetype='application/json')

def now_playing(request, pid):
  party = Party.objects.get(pk=pid)
  playing = party.now_playing
  if playing:
    result = cjson.encode(playing.to_hash())
  else:
    result = '{"status":"Failure"}'
  return HttpResponse(result, mimetype='application/json')


def queue(request, pid):
  party = Party.objects.get(pk=pid)
  result = cjson.encode([d.to_hash() for d in party.sorted_queue])
  return HttpResponse(result, mimetype='application/json')

def get_next_song(request, pid):
  party = Party.objects.get(pk=pid)
  song = party.pop()
  party.save()
  if song:
    if 'access_token' in request.session:
      data = urllib.urlencode({
        'message': 'started playing %s - %s on http://spunby.me' % (song.artist, song.title)
      })
      urllib.urlopen('https://graph.facebook.com/me/feed?access_token=%s' % request.session['access_token'], data)
    result = cjson.encode(song.to_hash())
  else:
    result = cjson.encode({'status':'Failure'})
  return HttpResponse(result, mimetype='application/json')
