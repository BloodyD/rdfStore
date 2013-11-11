from rdf_store.decorators import render_to
from django.http import HttpResponse

@render_to("index.html")
def index(request):
  return {}
