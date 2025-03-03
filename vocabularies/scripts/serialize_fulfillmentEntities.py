# script to convert fulfillmentEntities.csv to json-ld
# requires libraries/plugins: rdflib, rdflib-jsonld
from rdflib.namespace import SKOS
from rdflib import Namespace, Graph, Literal, URIRef
import csv
from utils import sort_and_write_graph_to_file


f = open('../csv/fulfillmentEntities.csv')
reader = csv.DictReader(f)

nypl = Namespace('http://data.nypl.org/nypl-core/')
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
g = Graph()

fulfillmentUriPrefix = URIRef('http://data.nypl.org/fulfillment/')
locationUriPrefix = URIRef('http://data.nypl.org/locations/')

for r in reader:
    id = Literal(r['@id'])
    prefLabel = Literal(r['skos:prefLabel'])
    estimatedTime = Literal(r['nypl:estimatedTime'])
    location = r['nypl:location']
    fulfillmentEntity = fulfillmentUriPrefix + id

    g.add((fulfillmentEntity, nypl.estimatedTime, estimatedTime))
    g.add((fulfillmentEntity, SKOS.prefLabel, prefLabel))
    if location is not None and len(location) > 0:
        fullLocation = locationUriPrefix + location
        g.add((fulfillmentEntity, nypl.location, fullLocation))

context = {
    "nypl": "http://data.nypl.org/nypl-core/",
    "fulfillment": "http://data.nypl.org/fulfillment/",
    "nyplLocation": "http://data.nypl.org/locations/",
    "skos": "http://www.w3.org/2004/02/skos/core#"
}
sort_and_write_graph_to_file(g, context, 'fulfillmentEntities')

f.close()
