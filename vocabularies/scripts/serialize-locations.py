# script to convert locations.csv to json-ld
# requires libraries/plugins: rdflib, rdflib-jsonld

from rdflib.namespace import RDF, SKOS
from rdflib import Namespace, Graph
import rdflib
import csv
import m2Utils
from utils import sort_and_write_graph_to_file

f = open('../csv/locations.csv')
reader = csv.DictReader(f)

nypl = Namespace('http://data.nypl.org/nypl-core/')
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
dcterms = Namespace('http://purl.org/dc/terms/')
nyplLocation = rdflib.URIRef('http://data.nypl.org/locations/')
nyplOrg = rdflib.URIRef('http://data.nypl.org/orgs/')
recapCustomerCode = rdflib.URIRef('http://data.nypl.org/recapCustomerCodes/')
m2CustomerCode = m2Utils.custCode
m2CodesByLocation = m2Utils.buildAssociatedLocations()


g = Graph()

for r in reader:
    id = r['skos:notation']
    type = 'nypl:Location'
    preflabel = rdflib.Literal(r['skos:prefLabel'])
    altlabel = rdflib.Literal(r['skos:altLabel'])
    notation = rdflib.Literal(r['skos:notation'])
    collectionType = r['nypl:collectionType'].split(';')
    deliveryLocationType = r['nypl:deliveryLocationType'].split(';')
    actualLocation = r['nypl:actualLocation']
    location = nyplLocation + str(id)
    deliverableTo = r['nypl:deliverableTo'].split(';')
    requestable = r['nypl:requestable']
    slug = r['nypl:locationsSlug']
    allowSierraHold = r['nypl:allowSierraHold']
    deliverableToResolution = r['nypl:deliverableToResolution']

    g.add((location, RDF.type, nypl.Location))
    g.add((location, SKOS.prefLabel, preflabel))
    g.add((location, SKOS.altLabel, altlabel))
    g.add((location, SKOS.notation, notation))

    if r['nypl:collectionAccessType'] != '':
        collectionAccessType = rdflib.Literal(r['nypl:collectionAccessType'])
        g.add((location, nypl.collectionAccessType, collectionAccessType))

    if deliverableToResolution != '':
        deliverableToResolution = rdflib.Literal(deliverableToResolution)
        g.add(
            (location, nypl.deliverableToResolution, deliverableToResolution))
    if r['dcterms:isPartOf'] != '':
        sublocationOf = nyplLocation + r['dcterms:isPartOf']
        g.add((location, dcterms.isPartOf, sublocationOf))
    if r['nypl:owner'] != '':
        owner = nyplOrg + str(r['nypl:owner'])
        g.add((location, nypl.owner, owner))
    if actualLocation != '':
        actualLocation = rdflib.Literal(actualLocation)
        g.add((location, nypl.actualLocation, actualLocation))
    if slug != '':
        slug = rdflib.Literal(slug)
        g.add((location, nypl.locationsSlug, slug))
    for c in collectionType:
        if c != '':
            c = rdflib.Literal(c)
            g.add((location, nypl.collectionType, c))
    for d in deliveryLocationType:
        if d != '':
            d = rdflib.Literal(d)
            g.add((location, nypl.deliveryLocationType, d))
    if requestable != '':
        requestable = rdflib.Literal(requestable, datatype="XSD:boolean")
        g.add((location, nypl.requestable, requestable))
    if allowSierraHold != '':
        allowSierraHold = rdflib.Literal(
            allowSierraHold, datatype="XSD:boolean")
        g.add((location, nypl.allowSierraHold, allowSierraHold))
    if r['nypl:deliverableTo'] != '':
        for d in deliverableTo:
            if d != '':
                d = nyplLocation + d.strip()
                g.add((location, nypl.deliverableTo, d))
    if r['nypl:recapCustomerCode'] != '':
        custcode = recapCustomerCode + str(r['nypl:recapCustomerCode'])
        g.add((location, nypl.recapCustomerCode, custcode))
    if m2CodesByLocation.get(id) and m2CodesByLocation.get(id) != '':
        m2CustCode = m2CustomerCode + str(m2CodesByLocation[id])
        g.add((location, nypl.m2CustomerCode, m2CustCode))

context = {"dcterms": "http://purl.org/dc/terms/",
           "nypl": "http://data.nypl.org/nypl-core/",
           "skos": "http://www.w3.org/2004/02/skos/core#",
           "nyplLocation": "http://data.nypl.org/locations/",
           "recapCustomerCode": "http://data.nypl.org/recapCustomerCodes"}

sort_and_write_graph_to_file(g, context, 'locations')

f.close()
