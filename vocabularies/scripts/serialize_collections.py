
# script to convert collections.csv to json-ld
# requires libraries/plugins: rdflib, rdflib-jsonld

from rdflib.namespace import RDF, SKOS
from rdflib import Namespace, Graph
import rdflib
import csv
import m2Utils
from utils import sort_and_write_graph_to_file

f = open('../csv/collections.csv')
reader = csv.DictReader(f)

nypl = Namespace('http://data.nypl.org/nypl-core/')
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
nyplLocation = rdflib.URIRef('http://data.nypl.org/locations/')
nyplOrg = rdflib.URIRef('http://data.nypl.org/orgs/')
recapCustomerCode = rdflib.URIRef('http://data.nypl.org/recapCustomerCodes/')
m2CustomerCode = m2Utils.custCode
m2CodesByLocation = m2Utils.buildAssociatedLocations()


g = Graph()

for r in reader:
    id = r['skos:notation']
    type = 'nypl:Collection'
    preflabel = rdflib.Literal(r['skos:prefLabel'])
    holdingLocations = r['nypl:holdingLocations'].split(';')
    collection = ...

    g.add((collection, RDF.type, nypl.Location))
    g.add((collection, SKOS.prefLabel, preflabel))
    g.add((collection, SKOS.notation, notation))

 
context = {
           "nypl": "http://data.nypl.org/nypl-core/",
           "skos": "http://www.w3.org/2004/02/skos/core#",
           "nyplLocation": "http://data.nypl.org/locations/",
           "recapCustomerCode": "http://data.nypl.org/recapCustomerCodes"}

sort_and_write_graph_to_file(g, context, 'collections')

f.close()
