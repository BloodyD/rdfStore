from rdf_store.decorators import render_to
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from django.core.urlresolvers import reverse

from store import RDFStorage
from store.forms import LoadForm, QueryForm
from xml.dom import minidom
import simplejson as json


INDEX = HttpResponseRedirect("/")

@render_to("index.html")
def query(request):
  if request.method != "POST": return INDEX

  form = QueryForm(request.POST)
  result = {"load_form":LoadForm(), "query_form": form}
  if form.is_valid():
    rdf_query = form.cleaned_data.get("rdf_query")
    format = form.cleaned_data.get("output_type", "xml")

    if not rdf_query:
      messages.add_message(request, messages.ERROR, "Please enter a query!")
      return result
    try:
      queryResult = RDFStorage().query(rdf_query)
      stringResult = queryResult.serialize(format = format)
      if format == "xml":
        xml = minidom.parseString(stringResult)
        stringResult = xml.toprettyxml()
      elif format == "json":
        stringResult = json.dumps(json.loads(stringResult), sort_keys = False, indent = 4)
      result.update({"result" : stringResult})
    except Exception, e:
      result.update({"exception" : e})

  return result
    

@render_to("index.html")
def load(request):
  if request.method != "POST": return INDEX
  form = LoadForm(request.POST)
  result = {"load_form":form, "query_form": QueryForm()}
  if form.is_valid():
    load_type = form.cleaned_data.get("load_type")
    rdf_content = form.cleaned_data.get("rdf_content")
    if not rdf_content: 
      messages.add_message(request, messages.ERROR, "Please enter some content!")
      return result
    try:
      storage = RDFStorage()
      storage.storeData(rdf_content, load_type)
      messages.add_message(request, messages.INFO, "New RDFStorage could be successfully created!")
    except Exception, e:
      result.update({"exception": e})

  return result
