from common.models import Party

def party_vote(request, slug):
  party = get_object_or_404(Party, slug=slug)
  context = RequestContext(request, {
    'party': party
  })
  return render_to_response('mobile.html', context)
