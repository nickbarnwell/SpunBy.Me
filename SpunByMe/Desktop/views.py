from django.http import HttpResponse
from django.template import Context, loader

def party(request, slug):
  t = loader.get_template('party.html')
  c = Context({})
  return HttpResponse(t.render(c))
