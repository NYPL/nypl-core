# script to convert locations.csv to json-ld
# requires libraries/plugins: rdflib, rdflib-jsonld

from rdflib.namespace import RDF, SKOS
from rdflib import Namespace, Graph
import rdflib
import csv
from utils import sort_and_write_graph_to_file

f = open('../csv/patronTypes.csv')
reader = csv.DictReader(f)

nypl = Namespace('http://data.nypl.org/nypl-core/')
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
nyplOrg = rdflib.URIRef('http://data.nypl.org/orgs/')
nyplPatronType = rdflib.URIRef('http://data.nypl.org/patronTypes/')
nyplLocation = rdflib.URIRef('http://data.nypl.org/locations/')


g = Graph()

for r in reader:
    id = r['skos:notation']
    type = 'nypl:PatronType'
    preflabel = rdflib.Literal(r['skos:prefLabel'])
    notation = rdflib.Literal(r['skos:notation'])
    access = access = r['nypl:deliveryLocationAccess'].split(';')
    deliveryLocation = r['nypl:scholarRoom']
    ptype = nyplPatronType + str(id)

    g.add((ptype, RDF.type, nypl.PatronType))
    g.add((ptype, SKOS.prefLabel, preflabel))
    g.add((ptype, SKOS.notation, notation))
    if r['nypl:scholarRoom'] is not None:
        g.add((ptype, nypl.scholarRoom, nyplLocation +
               rdflib.Literal(deliveryLocation)))
    if r['nypl:deliveryLocationAccess'] != '':
        for a in access:
            if a != '':
                g.add((ptype, nypl.deliveryLocationAccess, rdflib.Literal(a)))

context = {"nypl": "http://data.nypl.org/nypl-core/",
           "skos": "http://www.w3.org/2004/02/skos/core#",
           "nyplOrg": "http://data.nypl.org/orgs/",
           "ptype": "http://data.nypl.org/patronTypes/",
           "nyplLocation": 'http://data.nypl.org/locations/'}

sort_and_write_graph_to_file(g, context, 'patronTypes')

f.close()
