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
    altlabel = rdflib.Literal(r['skos:altLabel'])
    notation = rdflib.Literal(r['skos:notation'])
    status = nyplStatus + str(id)
    requestable = r['nypl:requestable']
    
    g.add( (status, RDF.type, nypl.Status))
    g.add( (status, SKOS.prefLabel, preflabel))
    g.add( (status, SKOS.altLabel, altlabel))
    g.add( (status, SKOS.notation, notation))
    if r['skos:note'] != '':
        note = rdflib.Literal(r['skos:note'])
        g.add( (status, SKOS.note, note))
    if requestable != '':
        requestable = rdflib.Literal(requestable, datatype="XSD:boolean")
        g.add ( (status, nypl.requestable, requestable) )

z = open('statuses.json', 'wb')

context = {"nypl": "http://data.nypl.org/nypl-core/",
           "skos": "http://www.w3.org/2004/02/skos/core#", 
           "nyplStatus": "http://data.nypl.org/statuses/"}
z.write(g.serialize(format="json-ld", context=context))

z.close()

