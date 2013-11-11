from rdflib import plugin, URIRef, Literal, Graph
from rdflib.store import Store
import os

DEFAULT_DB = "rdfDatabase.sqlite"
IDENTIFIER = "RDFStorage"

class RDFStorage(object):
  name = DEFAULT_DB
  def __init__(self):
    super(RDFStorage, self).__init__()
    store = plugin.get("SQLAlchemy", Store)(identifier=IDENTIFIER)
    self.graph = Graph(store, identifier=IDENTIFIER)

  def __del__(self):
    self.close()

  def open(self, dbName = DEFAULT_DB, create = True):
    if not dbName: return -1
    self.name = dbName
    if not dbName.startswith("sqlite:///"):
      dbName = "sqlite:///" + dbName
    return self.graph.open(dbName, create)

  def _delete_old(self, fName):
    if os.path.exists(fName):
      os.remove(fName)

  def close(self):
    self.graph.close()

  def storeData(self, data, format = "n3"):
    self._delete_old(self.name)
    self.open(self.name)
    self.graph.parse(data = data, format = format)

  def query(self, qString):
    self.open(self.name)
    return self.graph.query(qString)


# ident = URIRef("rdflib_test")
# uri = Literal("sqlite:///test.sqlite")
# turleFile = 'aufgabe1.ttl'

# store = plugin.get("SQLAlchemy", Store)(identifier=ident)
# graph = Graph(store, identifier=ident)

# graph.open(uri, create=True)
# cont = open(turleFile).read()
# graph.parse(data = cont, format='n3')


# graph.close()

# qres = graph.query("SELECT ?role ?name WHERE{?role dbpp:portrayer ?name}")
# print qres.serialize(format = "json")
# for row in qres:
#   print "%s portrayes %s" %row
