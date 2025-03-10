# script to convert accessMessages.csv (OPAC messages) to json-ld
# requires libraries/plugins: rdflib, rdflib-jsonld

from rdflib.namespace import RDF, SKOS
from rdflib import Namespace, Graph
import rdflib
import csv
from utils import sort_and_write_graph_to_file


f = open('../csv/accessMessages.csv')
reader = csv.DictReader(f)

nypl = Namespace('http://data.nypl.org/nypl-core/')
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
# dcterms = Namespace('http://purl.org/dc/terms/')
nyplAccessMessage = rdflib.URIRef('http://data.nypl.org/accessMessages/')

g = Graph()

for r in reader:
    id = r['skos:notation']
    type = 'nypl:AccessMessage'
    preflabel = rdflib.Literal(r['skos:prefLabel'])
    altlabel = rdflib.Literal(r['skos:altLabel'])
    notation = rdflib.Literal(r['skos:notation'])
#    locationType = r['nypl:locationType'].split(';')
    accessMessage = nyplAccessMessage + str(id)

    g.add((accessMessage, RDF.type, nypl.AccessMessage))
    g.add((accessMessage, SKOS.prefLabel, preflabel))
    g.add((accessMessage, SKOS.altLabel, altlabel))
    g.add((accessMessage, SKOS.notation, notation))
#    for l in locationType:
#        if l != '':
#            loc = rdflib.Literal(l)
#            g.add( (accessMessage, nypl.locationType, loc))

context = {"nypl": "http://data.nypl.org/nypl-core/",
           "skos": "http://www.w3.org/2004/02/skos/core#",
           "nyplAccessMessage": "http://data.nypl.org/accessMessages/"}
sort_and_write_graph_to_file(g, context, 'accessMessages')
