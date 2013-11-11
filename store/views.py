from rdf_store.decorators import render_to
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from django.core.urlresolvers import reverse

from store import RDFStorage
from xml.dom import minidom
import simplejson as json


INDEX = HttpResponseRedirect("/")

@render_to("index.html")
def query(request):
  if request.method != "POST": return INDEX

  rdf_query = request.POST.get("rdf-query")
  format = request.POST.get("output-type", "xml")

  if not rdf_query:
    messages.add_message(request, messages.ERROR, "Please enter a query!")
    return INDEX

  try:
    result = RDFStorage().query(rdf_query)
    stringResult = result.serialize(format = format)
    if format == "xml":
      xml = minidom.parseString(stringResult)
      stringResult = xml.toprettyxml()
    elif format == "json":
      stringResult = json.dumps(json.loads(stringResult), sort_keys = False, indent = 4)
    return {"result" : stringResult, "format" : format}
  except Exception, e:
    return {"exception" : e}
    

@render_to("index.html")
def load(request):
  if request.method != "POST": return INDEX

  rdf_type = request.POST.get("rdf-type")
  rdf_content = request.POST.get("rdf-content")
  if not rdf_content: 
    messages.add_message(request, messages.ERROR, "Please enter some content!")
    return INDEX
  try:
    storage = RDFStorage()
    storage.storeData(rdf_content, rdf_type)
    messages.add_message(request, messages.INFO, "New RDFStorage could be successfully created!")
    return INDEX
  except Exception, e:
    return {"exception": e}
