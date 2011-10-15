from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import Context, RequestContext, loader
import urllib2
from common.models import Party, User, Song
import cjson
from desktop.forms import PartyForm

FACEBOOK_APP_ID = '252389068144629'
FACEBOOK_API_SECRET = '794cb30ba61fb6609bdd81a9b61eead2'
OAUTH_REDIRECT_URI = 'http://spunby.me/login/'

def index(request):
  if request.session.get('access_token', None) is None:
    context = RequestContext(request, {
      'login_url': 'https://www.facebook.com/dialog/oauth?client_id=%s&redirect_uri=%s' \
        % (FACEBOOK_APP_ID, OAUTH_REDIRECT_URI)
    })
    return render_to_response('landing.html', context)
  else:
    context = RequestContext(request, {'form':PartyForm(), 'user':request.session['user'], 'rooms':[r for r in Party.objects.filter(owner=request.session['user'])]})
    return render_to_response('landing.html', context)

class MockParty:
  pass
def dashboard(request):
  party = MockParty()
  party.id = 1
  party.viewer_url = 'http://google.com'
  return render_to_response('dashboard.html', RequestContext(request, {'party':party}))

def party_dash(request, slug):
  party = Party.objects.get(slug=slug)
  if request.session['user'] != party.owner:
    return HttpResponse('Sorry, you\'re not authorized to view this page')
  return render_to_response('dashboard.html', RequestContext(request, {'party':party}))

def login(request):
  if request.GET.get('error') is not None:
    return render_to_response('login_error.html', Context({
      'error_reason': request.GET.get('error_reason'),
      'error_description': request.GET.get('error_description')
    }))
  else:
    oauth_url = 'https://graph.facebook.com/oauth/access_token?' + \
                'client_id=%s&redirect_uri=%s&client_secret=%s&code=%s' % \
                (FACEBOOK_APP_ID, OAUTH_REDIRECT_URI, FACEBOOK_API_SECRET, \
                request.GET.get('code'))
    response = urllib2.urlopen(oauth_url).read()
    access_token = response.split('=')[1].split('&')[0]
    request.session['access_token'] = access_token
    me = cjson.decode(
      urllib2.urlopen(
        'https://graph.facebook.com/me/?access_token=%s' % access_token).read())
    user, created = User.objects.get_or_create(first_name=me['first_name'], last_name = me['last_name'], fb_username = me['username'])
    
    request.session['user'] = user
    return redirect('desktop.views.index')

def new_party(request):
  if request.method == 'POST':
    form = PartyForm(request.POST)
    if form.is_valid():
      user = User.objects.get(fb_username=request.session['user'].fb_username)
      p, created = Party.objects.get_or_create(name=form.cleaned_data['name'], owner=user)
      s=Song.add_song('The Flaming Lips', 'Test')
      QueueData(song=s, party=p).save()

      return redirect(p)
    else:
      redirect
  else:
    return HttpResponse('lolno')
