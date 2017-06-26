# script to convert statuses.csv to json-ld
# requires libraries/plugins: rdflib, rdflib-jsonld

from rdflib.namespace import RDF, SKOS
from rdflib import Namespace, Graph, plugin
from rdflib.serializer import Serializer
import rdflib
import csv

f = open('statuses.csv')
reader = csv.DictReader(f)

nypl = Namespace('http://data.nypl.org/nypl-core/')
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
nyplStatus = rdflib.URIRef('http://data.nypl.org/statuses/')

g = Graph()

for r in reader:
    id = r['id']
    type = 'nypl:Status'
    preflabel = rdflib.Literal(r['skos:prefLabel'])
    notation = rdflib.Literal(r['skos:notation'])
    status = nyplStatus + str(id)
    
    g.add( (status, RDF.type, nypl.Status))
    g.add( (status, SKOS.prefLabel, preflabel))
    g.add( (status, SKOS.notation, notation))

z = open('sierra-status-codes.json', 'wb')

context = {"nypl": "http://data.nypl.org/nypl-core/",
           "skos": "http://www.w3.org/2004/02/skos/core#", 
           "nyplStatus": "http://data.nypl.org/statuses/"}
z.write(g.serialize(format="json-ld", context=context))

z.close()

