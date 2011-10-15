from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import Context, RequestContext, loader

from common.models import Party

def party_vote(request, slug):
  party = get_object_or_404(Party, slug=slug)
  context = RequestContext(request, {
    'party': party
  })
  return render_to_response('mobile.html', context)
