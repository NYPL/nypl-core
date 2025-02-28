# script to convert recordTypes.csv to json-ld
# requires libraries/plugins: rdflib, rdflib-jsonld

from rdflib.namespace import RDF, SKOS
from rdflib import Namespace, Graph
import rdflib
import csv
from utils import sort_and_write_graph_to_file


def serialize(data_type):
    f = open(f'../csv/{data_type}s.csv')
    reader = csv.DictReader(f)

    nypl = Namespace('http://data.nypl.org/nypl-core/')
    nyplDataType = rdflib.URIRef(f'http://data.nypl.org/{data_type}/')

    g = Graph()

    for r in reader:
        id = r['skos:notation']
        preflabel = rdflib.Literal(r['skos:prefLabel'])
        altlabel = rdflib.Literal(r['skos:altLabel'])
        notation = rdflib.Literal(r['skos:notation'])
        dataType = nyplDataType + str(id)

        g.add((dataType, RDF.type, nypl[data_type]))
        g.add((dataType, SKOS.prefLabel, preflabel))
        g.add((dataType, SKOS.altLabel, altlabel))
        g.add((dataType, SKOS.notation, notation))

    context = {
        "nypl": "http://data.nypl.org/nypl-core/",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        data_type: f'http://data.nypl.org/{data_type}/'}

    sort_and_write_graph_to_file(g, context, data_type+'s')

    f.close()