from rdflib.namespace import RDF, SKOS
from rdflib import Namespace, Graph, plugin
from rdflib.serializer import Serializer
import rdflib
import csv

f = open('../csv/m2CustomerCodes.csv')
reader = csv.DictReader(f)

nypl = Namespace('http://data.nypl.org/nypl-core/')
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
nyplOrg = rdflib.URIRef('http://data.nypl.org/orgs/')
custCode = rdflib.URIRef('http://data.nypl.org/m2CustomerCodes/')

g = Graph()

for r in reader:
    id = r['skos:notation']
    type = 'nypl:m2CustomerCode'
    prefLabel = rdflib.Literal(r['skos:prefLabel'])
    notation = rdflib.Literal(r['skos:notation'])
    deliverableTo = r['nypl:deliverableTo'].split(';')
    requestable = r['nypl:requestable']
    m2CustomerCode = custCode + str(id)

    g.add( (m2CustomerCode, RDF.type, nypl.m2CustomerCode))
    g.add( (m2CustomerCode, SKOS.prefLabel, prefLabel))
    g.add( (m2CustomerCode, SKOS.notation, notation))
    if requestable != '':
        requestable = rdflib.Literal(requestable, datatype="XSD:boolean")
        g.add( (m2CustomerCode, nypl.requestable, requestable) )
    if r['nypl:deliverableTo'] != '':
        for d in deliverableTo:
            if d != '':
                d = custCode + d.strip()
                g.add( (m2CustomerCode, nypl.deliverableTo, d))

z = open('../json-ld/m2CustomerCodes.json', 'wb')

context = {"nypl": "http://data.nypl.org/nypl-core/",
           "skos": "http://www.w3.org/2004/02/skos/core#",
           "nyplOrg": "http://data.nypl.org/orgs/",
           "customerCode": "http://data.nypl.org/m2CustomerCodes"}
z.write(g.serialize(format="json-ld", context=context, encoding="utf-8"))

z.close()
f.close()
