# script to convert catalogItemTypes.csv to json-ld
# requires libraries/plugins: rdflib, rdflib-jsonld

from rdflib.namespace import RDF, SKOS
from rdflib import Namespace, Graph, plugin
from rdflib.serializer import Serializer
import rdflib
import csv

f = open('../csv/catalogItemTypes.csv')
reader = csv.DictReader(f)

nypl = Namespace('http://data.nypl.org/nypl-core/')
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
nyplCatalogItemType = rdflib.URIRef('http://data.nypl.org/catalogItemTypes/')

g = Graph()

for r in reader:
    id = r['skos:notation']
    type = 'nypl:CatalogItemType'
    preflabel = rdflib.Literal(r['skos:prefLabel'])
    notation = rdflib.Literal(r['skos:notation'])
    collectionType = r['nypl:collectionType'].split(';')
    note = r['skos:note']
    requestable = r['nypl:requestable']
    catalogItemType = nyplCatalogItemType + str(id)
    
    g.add( (catalogItemType, RDF.type, nypl.CatalogItemType))
    g.add( (catalogItemType, SKOS.prefLabel, preflabel))
    g.add( (catalogItemType, SKOS.notation, notation))
    if note != '':
        note = rdflib.Literal(note)
        g.add ( (catalogItemType, SKOS.note, note) )
    if requestable != '':
        requestable = rdflib.Literal(requestable, datatype="XSD:boolean")
        g.add ( (catalogItemType, nypl.requestable, requestable) )
    for l in collectionType:
        if l != '':
            l = rdflib.Literal(l)
            g.add( (catalogItemType, nypl.collectionType, l))

z = open('../json-ld/catalogItemTypes.json', 'wb')

context = {"nypl": "http://data.nypl.org/nypl-core/",
           "skos": "http://www.w3.org/2004/02/skos/core#",
           "nyplCatalogItemTypes": "http://data.nypl.org/catalogItemTypes/"}
z.write(g.serialize(format="json-ld", context=context, encoding="utf-8"))

z.close()
f.close()
