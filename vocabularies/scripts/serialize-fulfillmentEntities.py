# script to convert fulfillmentEntities.csv to json-ld
# requires libraries/plugins: rdflib, rdflib-jsonld
from rdflib.namespace import RDF, SKOS
from rdflib import Namespace, Graph, plugin
from rdflib.serializer import Serializer
import rdflib
import csv

import csv
import json

f = open('../csv/fulfillmentEntities.csv')
reader = csv.DictReader(f)

print(json.dump())

for r in reader:
    id = r['@id']
    label = r['label']
    estimatedTime = r['estimatedTime']

