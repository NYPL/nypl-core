# script to convert locations.csv to json-ld
# requires libraries/plugins: rdflib, rdflib-jsonld

from rdflib.namespace import RDF, SKOS
from rdflib import Namespace, Graph, plugin
from rdflib.serializer import Serializer
import rdflib
import csv

f = open('../csv/patronTypes.csv')
reader = csv.DictReader(f)

nypl = Namespace('http://data.nypl.org/nypl-core/')
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
nyplOrg = rdflib.URIRef('http://data.nypl.org/orgs/')
nyplPatronType = rdflib.URIRef('http://data.nypl.org/patronTypes/')

g = Graph()

for r in reader:
    id = r['skos:notation']
    type = 'nypl:PatronType'
    preflabel = rdflib.Literal(r['skos:prefLabel'])
    notation = rdflib.Literal(r['skos:notation'])
    access = access = r['nypl:deliveryLocationAccess'].split(';')
    deliveryLocations = r['nypl:deliverableTo']
    ptype = nyplPatronType + str(id)

    g.add((ptype, RDF.type, nypl.PatronType))
    g.add((ptype, SKOS.prefLabel, preflabel))
    g.add((ptype, SKOS.notation, notation))
    if r['nypl:deliverableTo'] != '':
        g.add((ptype, nypl.deliverableTo, rdflib.Literal(deliveryLocations)))
    if r['nypl:deliveryLocationAccess'] != '':
        for a in access:
            if a != '':
                g.add((ptype, nypl.deliveryLocationAccess, rdflib.Literal(a)))

z = open('../json-ld/patronTypes.json', 'wb')

context = {"nypl": "http://data.nypl.org/nypl-core/",
           "skos": "http://www.w3.org/2004/02/skos/core#",
           "nyplOrg": "http://data.nypl.org/orgs/",
           "ptype": "http://data.nypl.org/patronTypes/"}
z.write(g.serialize(format="json-ld", context=context, encoding="utf-8"))

z.close()
f.close()
