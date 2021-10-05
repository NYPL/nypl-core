# script to convert locations.csv to json-ld
# requires libraries/plugins: rdflib, rdflib-jsonld

from rdflib.namespace import RDF, SKOS
from rdflib import Namespace, Graph, plugin
from rdflib.serializer import Serializer
import rdflib
import csv

f = open('../csv/icode2.csv')
reader = csv.DictReader(f)

nypl = Namespace('http://data.nypl.org/nypl-core/')
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
nyplOrg = rdflib.URIRef('http://data.nypl.org/orgs/')
nyplIcode2 = rdflib.URIRef('http://data.nypl.org/icode2/')

g = Graph()

for r in reader:
    id = r['skos:notation']
    type = 'nypl:Icode2'
    preflabel = rdflib.Literal(r['skos:prefLabel'])
    notation = rdflib.Literal(r['skos:notation'])
    suppressed = rdflib.Literal(r['nypl:suppressed'], datatype="XSD:boolean")
    icode2 = nyplIcode2 + str(id)
    
    g.add( (icode2, RDF.type, nypl.Icode2))
    g.add( (icode2, SKOS.prefLabel, preflabel))
    g.add( (icode2, SKOS.notation, notation))
    g.add( (icode2, nypl.suppressed, suppressed))
    if r['skos:note'] != '':
        note = rdflib.Literal(r['skos:note'])
        g.add( (icode2, SKOS.note, note))

z = open('../json-ld/icode2.json', 'wb')

context = {"nypl": "http://data.nypl.org/nypl-core/",
           "skos": "http://www.w3.org/2004/02/skos/core#", 
           "nyplOrg": "http://data.nypl.org/orgs/",
           "icode2": "http://data.nypl.org/icode2/"}
z.write(g.serialize(format="json-ld", context=context, encoding="utf-8"))

z.close()
f.close()

