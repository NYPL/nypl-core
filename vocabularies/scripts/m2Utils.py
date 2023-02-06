import rdflib
import csv

custCode = rdflib.URIRef('http://data.nypl.org/m2CustomerCodes/')
customerCodeFilename = '../csv/m2CustomerCodes.csv'

def buildAssociatedLocations():
    map = {}
    f = open(customerCodeFilename)
    reader = csv.DictReader(f)
    for r in reader:
        map[r['Associated Sierra location']] = r['skos:notation']
    f.close
    return map
