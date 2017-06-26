# script to convert locations.csv to json-ld
# requires libraries/plugins: rdflib, rdflib-jsonld

from rdflib.namespace import RDF, SKOS
from rdflib import Namespace, Graph, plugin
from rdflib.serializer import Serializer
import rdflib
import csv

f = open('locations.csv')
reader = csv.DictReader(f)

nypl = Namespace('http://data.nypl.org/nypl-core/')
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
dcterms = Namespace('http://purl.org/dc/terms/')
nyplLocation = rdflib.URIRef('http://data.nypl.org/locations/')
nyplOrg = rdflib.URIRef('http://data.nypl.org/orgs/')
recapCustomerCode = rdflib.URIRef('http://data.nypl.org/recapCustomerCodes/')

g = Graph()

for r in reader:
    id = r['skos:notation']
    type = 'nypl:Location'
    preflabel = rdflib.Literal(r['skos:prefLabel'])
    notation = rdflib.Literal(r['skos:notation'])
    locationType = r['nypl:locationType'].split(';')
    actualLocation = r['nypl:actualLocation']
    location = nyplLocation + str(id)
    deliverableTo = r['nypl:deliverableTo'].split(';')
    requestable = r['nypl:requestable']
    
    g.add( (location, RDF.type, nypl.Location))
    g.add( (location, SKOS.prefLabel, preflabel))
    g.add( (location, SKOS.notation, notation))
    if r['dcterms:isPartOf'] != '':
        sublocationOf = nyplLocation + r['dcterms:isPartOf']
        g.add( (location, dcterms.isPartOf, sublocationOf))
    if r['nypl:owner'] != '':
        owner = nyplOrg + str(r['nypl:owner'])
        g.add( (location, nypl.owner, owner))
    if actualLocation != '':
        actualLocation = rdflib.Literal(actualLocation)
        g.add ( (location, nypl.actualLocation, actualLocation) )
    for l in locationType:
        if l != '':
            l = rdflib.Literal(l)
            g.add( (location, nypl.locationType, l))
    if requestable != '':
        requestable = rdflib.Literal(requestable, datatype="XSD:boolean")
        g.add ( (location, nypl.requestable, requestable) )
    if r['nypl:deliverableTo'] != '':
        for d in deliverableTo:
            if d != '':
                d = nyplLocation + d.strip()
                g.add( (location, nypl.deliverableTo, d))
    if r['nypl:recapCustomerCode'] != '':
        custcode = recapCustomerCode + str(r['nypl:recapCustomerCode'])
        g.add( (location, nypl.recapCustomerCode, custcode))

z = open('locations.json', 'wb')

context = {"dcterms": "http://purl.org/dc/terms/",
           "nypl": "http://data.nypl.org/nypl-core/",
           "skos": "http://www.w3.org/2004/02/skos/core#", 
           "nyplLocation": "http://data.nypl.org/locations/",
           "recapCustomerCode": "http://data.nypl.org/recapCustomerCodes"}
z.write(g.serialize(format="json-ld", context=context))

z.close()
f.close()
