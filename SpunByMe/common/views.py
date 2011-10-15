from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from common.models import * 
import cjson


def search(request):
  result = Song().search(request.GET.get('q'))
  return HttpResponse(cjson.encode(result), mimetype='application/json')

def add_song(request):
  artist = request.GET.get('artist')
  title = request.GET.get('title')
  s = Song().add_song(artist, title)
  result = cjson.encode(s.to_hash())
  return HttpResponse(result, mimetype='application/json')

def vote(request):
  party_id = int(request.GET.get('party_id'))
  song_id = int(request.GET.get('song_id'))
  vtype = request.GET.get('type')
  qd = QueueData().find_by_party_song(party_id, song_id)
  qd.vote(vtype)
  qd.save()
  return HttpResponse('{votes:%d}' % votes, mimetype='application/json')
