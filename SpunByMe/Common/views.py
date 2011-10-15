from django.http import HttpResponse
import pylast
import cjson

LASTFM_API_KEY = '522cc370a4cc1ee8029e065e08a168fb'
LASTFM_API_SECRET = 'b5115b3e49d6c1db271f73146d4ef413'

def search(request):
    network = pylast.LastFMNetwork(
      api_key=LASTFM_API_KEY, api_secret=LASTFM_API_SECRET)
    search = network.search_for_track('', request.GET.get('q'))
    tracks = search.get_next_page()
    result = [dict(title=t.get_title(), artist=str(t.get_artist())) for t in tracks]
    return HttpResponse(cjson.encode(result), mimetype='application/json')
