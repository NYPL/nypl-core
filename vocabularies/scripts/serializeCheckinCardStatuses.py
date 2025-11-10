# script to convert statuses.csv to json-ld
# requires libraries/plugins: rdflib, rdflib-jsonld

from rdflib.namespace import RDF, SKOS
from rdflib import Namespace, Graph
import rdflib
import csv
from utils import sort_and_write_graph_to_file


f = open('../csv/checkinCardStatuses.csv')
reader = csv.DictReader(f)

nypl = Namespace('http://data.nypl.org/nypl-core/')
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
nyplCheckinCardStatus = rdflib.URIRef(
    'http://data.nypl.org/checkinCardStatuses/')
nyplStatus = rdflib.URIRef('http://data.nypl.org/statuses/')

g = Graph()

for r in reader:
    type = 'nypl:checkinCardStatus'
    id = rdflib.Literal(r['skos:notation'])
    prefLabel = rdflib.Literal(r['skos:prefLabel'])
    itemStatus = rdflib.Literal(r['nypl:itemStatusMapping'])
    display = rdflib.Literal(r['nypl:display'], datatype="XSD:boolean")
    checkinCardStatus = nyplCheckinCardStatus + str(id)

    g.add((checkinCardStatus, RDF.type, nypl.CheckinCardStatus))
    g.add((checkinCardStatus, SKOS.notation, id))
    g.add((checkinCardStatus, SKOS.prefLabel, prefLabel))
    g.add((checkinCardStatus, nypl.display, display))
    g.add((checkinCardStatus, nypl.itemStatus, itemStatus))

context = {"nypl": "http://data.nypl.org/nypl-core/",
           "skos": "http://www.w3.org/2004/02/skos/core#",
           "nyplStatus": "http://data.nypl.org/checkinCardStatuses/"}

sort_and_write_graph_to_file(g, context, 'checkinCardStatuses')
