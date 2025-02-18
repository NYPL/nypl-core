from rdflib.namespace import RDF, SKOS
from rdflib import Namespace, Graph
from utils import sort_and_write_graph_to_file
import rdflib
import csv
import m2Utils

f = open(m2Utils.customerCodeFilename)
reader = csv.DictReader(f)

nypl = Namespace('http://data.nypl.org/nypl-core/')
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
nyplOrg = rdflib.URIRef('http://data.nypl.org/orgs/')
custCode = m2Utils.custCode

g = Graph()

for r in reader:
    id = r['skos:notation']
    type = 'nypl:m2CustomerCode'
    prefLabel = rdflib.Literal(r['skos:prefLabel'])
    notation = rdflib.Literal(r['skos:notation'])
    deliverableTo = r['nypl:deliverableTo'].split(';')
    requestable = r['nypl:requestable']
    m2CustomerCode = custCode + str(id)

    g.add((m2CustomerCode, RDF.type, nypl.m2CustomerCode))
    g.add((m2CustomerCode, SKOS.prefLabel, prefLabel))
    g.add((m2CustomerCode, SKOS.notation, notation))
    if requestable != '':
        requestable = rdflib.Literal(requestable, datatype="XSD:boolean")
        g.add((m2CustomerCode, nypl.requestable, requestable))
    if r['nypl:deliverableTo'] != '':
        for d in deliverableTo:
            if d != '':
                d = custCode + d.strip()
                g.add((m2CustomerCode, nypl.deliverableTo, d))

context = {"nypl": "http://data.nypl.org/nypl-core/",
           "skos": "http://www.w3.org/2004/02/skos/core#",
           "nyplOrg": "http://data.nypl.org/orgs/",
           "customerCode": "http://data.nypl.org/m2CustomerCodes"}

sort_and_write_graph_to_file(g, context, 'm2CustomerCodes')

f.close()
