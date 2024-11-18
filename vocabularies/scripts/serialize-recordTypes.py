# script to convert recordTypes.csv to json-ld
# requires libraries/plugins: rdflib, rdflib-jsonld

from rdflib.namespace import RDF, SKOS
from rdflib import Namespace, Graph
import rdflib
import csv

f = open('../csv/recordTypes.csv')
reader = csv.DictReader(f)

nypl = Namespace('http://data.nypl.org/nypl-core/')
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
nyplRecordType = rdflib.URIRef('http://data.nypl.org/recordTypes/')

g = Graph()

for r in reader:
    id = r['skos:notation']
    type = 'nypl:RecordType'
    preflabel = rdflib.Literal(r['skos:prefLabel'])
    altlabel = rdflib.Literal(r['skos:altLabel'])
    notation = rdflib.Literal(r['skos:notation'])
    recordType = nyplRecordType + str(id)

    g.add((recordType, RDF.type, nypl.RecordType))
    g.add((recordType, SKOS.prefLabel, preflabel))
    g.add((recordType, SKOS.altLabel, altlabel))
    g.add((recordType, SKOS.notation, notation))


z = open('../json-ld/recordTypes.json', 'wb')

context = {
    "nypl": "http://data.nypl.org/nypl-core/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "recordType": 'http://data.nypl.org/recordTypes/'}

z.write(g.serialize(format="json-ld", context=context, encoding="utf-8"))

z.close()
f.close()
