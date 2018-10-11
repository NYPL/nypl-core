# script to convert orgunits.csv to json-ld
# requires libraries/plugins: rdflib, rdflib-jsonld

from rdflib.namespace import RDF, SKOS
from rdflib import Namespace, Graph, plugin
from rdflib.serializer import Serializer
import rdflib
import csv

f = open('../csv/organizations.csv')
reader = csv.DictReader(f)

org = Namespace('http://www.w3.org/ns/org#')
nyplorg = rdflib.URIRef('http://data.nypl.org/orgs/')

g = Graph()

for r in reader:
    id = r['id']
    type = r['rdf:type']
    preflabel = rdflib.Literal(r['skos:prefLabel'])
    altlabel = r['skos:altLabel']
    unitof = r['org:unitOf'].split(',')
    orgunit = nyplorg + str(id)
    code = r['code']
    
    g.add( (orgunit, RDF.type, org.OrganizationalUnit))
    g.add( (orgunit, SKOS.prefLabel, preflabel))
    if altlabel != '':
        altlabel = rdflib.Literal(altlabel)
        g.add( (orgunit, SKOS.altLabel, altlabel))
    if code != '':
        code = rdflib.Literal(code)
        g.add ( (orgunit, SKOS.notation, code) )
    for u in unitof:
        if u != '':
            u = u.replace('http://data.nypl.org/orgs/', '')
            unit = nyplorg + u.strip()
            g.add( (orgunit, org.unitOf, unit))

z = open('../json-ld/organizations.json', 'wb')

context = {"org": "http://www.w3.org/ns/org#",
           "skos": "http://www.w3.org/2004/02/skos/core#", 
           "nyplOrg": "http://data.nypl.org/orgs/"}
z.write(g.serialize(format="json-ld", context=context))

z.close()
f.close()

