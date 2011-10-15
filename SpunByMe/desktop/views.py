from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import Context, loader
import urllib2

FACEBOOK_APP_ID = '252389068144629'
FACEBOOK_API_SECRET = '794cb30ba61fb6609bdd81a9b61eead2'
OAUTH_REDIRECT_URI = 'http://ryanewing.me/spunby/login/'

def index(request):
  if request.session.get('access_token', None) is None:
    context = Context({
      'login_url': 'https://www.facebook.com/dialog/oauth?client_id=%s&redirect_uri=%s' \
        % (FACEBOOK_APP_ID, OAUTH_REDIRECT_URI)
    })
    return render_to_response('landing.html', context)
  else:
    return HttpResponse('Your access token is %s' % request.session.get('access_token'))

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
  t = loader.get_template('party.html')
  c = Context({})
  return HttpResponse(t.render(c))
