# script to convert recordTypes.csv to json-ld
# requires libraries/plugins: rdflib, rdflib-jsonld

from rdflib.namespace import RDF, SKOS
from rdflib import Namespace, Graph
import rdflib
import csv
from utils import sort_and_write_graph_to_file


def serialize(data_type):
    f = open(f'../csv/{data_type}.csv')
    reader = csv.DictReader(f)

    nypl = Namespace('http://data.nypl.org/nypl-core/')
    nyplRecordType = rdflib.URIRef('http://data.nypl.org/recordTypes/')

    g = Graph()

    for r in reader:
        id = r['skos:notation']
        preflabel = rdflib.Literal(r['skos:prefLabel'])
        altlabel = rdflib.Literal(r['skos:altLabel'])
        notation = rdflib.Literal(r['skos:notation'])
        recordType = nyplRecordType + str(id)

        g.add((recordType, RDF.type, nypl.RecordType))
        g.add((recordType, SKOS.prefLabel, preflabel))
        g.add((recordType, SKOS.altLabel, altlabel))
        g.add((recordType, SKOS.notation, notation))

    context = {
        "nypl": "http://data.nypl.org/nypl-core/",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "recordType": 'http://data.nypl.org/recordTypes/'}

    sort_and_write_graph_to_file(g, context, 'recordTypes')

    f.close()