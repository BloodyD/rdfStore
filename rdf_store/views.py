from rdf_store.decorators import render_to
from django.http import HttpResponse
from store.forms import LoadForm, QueryForm

@render_to("index.html")
def index(request):
  return {
    "load_form":LoadForm(),
    "query_form": QueryForm()
  }
