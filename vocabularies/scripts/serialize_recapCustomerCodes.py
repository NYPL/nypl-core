from rdflib.namespace import RDF, SKOS
from rdflib import Namespace, Graph
import rdflib
import csv
from utils import sort_and_write_graph_to_file

f = open('../csv/recapCustomerCodes.csv')
reader = csv.DictReader(f)

nypl = Namespace('http://data.nypl.org/nypl-core/')
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
nyplOrg = rdflib.URIRef('http://data.nypl.org/orgs/')
custCode = rdflib.URIRef('http://data.nypl.org/recapCustomerCodes/')

g = Graph()

for r in reader:
    id = r['skos:notation']
    type = 'nypl:RecapCustomerCode'
    preflabel = rdflib.Literal(r['skos:prefLabel'])
    notation = rdflib.Literal(r['skos:notation'])
    deliverableTo = r['nypl:deliverableTo'].split(';')
    eddrequestable = r['nypl:eddRequestable']
    recapCustomerCode = custCode + str(id)

    g.add((recapCustomerCode, RDF.type, nypl.RecapCustomerCode))
    g.add((recapCustomerCode, SKOS.prefLabel, preflabel))
    g.add((recapCustomerCode, SKOS.notation, notation))
    if r['nypl:owner'] != '':
        owner = nyplOrg + str(r['nypl:owner'])
        g.add((recapCustomerCode, nypl.owner, owner))
    if eddrequestable != '':
        eddrequestable = rdflib.Literal(eddrequestable, datatype="XSD:boolean")
        g.add((recapCustomerCode, nypl.eddRequestable, eddrequestable))
    if r['nypl:deliverableTo'] != '':
        for d in deliverableTo:
            if d != '':
                d = custCode + d.strip()
                g.add((recapCustomerCode, nypl.deliverableTo, d))

context = {"nypl": "http://data.nypl.org/nypl-core/",
           "skos": "http://www.w3.org/2004/02/skos/core#",
           "nyplOrg": "http://data.nypl.org/orgs/",
           "recapCustomerCode": "http://data.nypl.org/recapCustomerCodes"}
sort_and_write_graph_to_file(g, context, 'recapCustomerCodes')


f.close()
