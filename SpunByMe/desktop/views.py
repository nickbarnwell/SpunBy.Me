from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import Context, RequestContext, loader
import urllib2
from common.models import Party

FACEBOOK_APP_ID = '252389068144629'
FACEBOOK_API_SECRET = '794cb30ba61fb6609bdd81a9b61eead2'
OAUTH_REDIRECT_URI = 'http://spunbyme.heroku.com/login/'

def index(request):
  if request.session.get('access_token', None) is None:
    context = RequestContext(request, {
      'login_url': 'https://www.facebook.com/dialog/oauth?client_id=%s&redirect_uri=%s' \
        % (FACEBOOK_APP_ID, OAUTH_REDIRECT_URI)
    })
    return render_to_response('landing.html', context)
  else:
    return HttpResponse('Your access token is %s' % request.session.get('access_token'))

def dashboard(request):
  return render_to_response('dashboard.html', RequestContext(request, {}))

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
    return redirect('desktop.views.index')

def party(request, slug):
  party = get_object_or_404(Party, slug=slug)
  context = RequestContext(request, {
    'party': party
  })
  return render_to_response('dashboard.html', context)

