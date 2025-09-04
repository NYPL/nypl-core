
# script to convert collections.csv to json-ld
# requires libraries/plugins: rdflib, rdflib-jsonld

from rdflib.namespace import SKOS
from rdflib import Namespace, Graph
import rdflib
import csv
from utils import sort_and_write_graph_to_file

f = open('../csv/collections.csv')
reader = csv.DictReader(f)

nypl = Namespace('http://data.nypl.org/nypl-core/')
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
nyplCollection = rdflib.URIRef('http://data.nypl.org/collections/')
nyplLocation = rdflib.URIRef('http://data.nypl.org/locations/')


g = Graph()

for r in reader:
    id = r['skos:notation']
    type = 'nypl:Collection'
    preflabel = rdflib.Literal(r['skos:prefLabel'])
    notation = rdflib.Literal(r['skos:notation'])

    holdingLocations = [loc.strip() for loc in r['nypl:holdingLocations'].split(';') if loc.strip()]

    collection = nyplCollection + str(id)

    g.add((collection, SKOS.notation, notation))
    g.add((collection, SKOS.prefLabel, preflabel))
    for loc in holdingLocations:
        g.add((collection, nyplLocation, nyplLocation + str(loc)))
 

 
context = {
           "nypl": "http://data.nypl.org/nypl-core/",
           "skos": "http://www.w3.org/2004/02/skos/core#",
           "nyplCollection": "http://data.nypl.org/collections/",
           "nyplLocation": "http://data.nypl.org/locations/",
}

sort_and_write_graph_to_file(g, context, 'collections')

f.close()
