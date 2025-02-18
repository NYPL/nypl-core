from collections import OrderedDict
import json


def sort_graph(graph, context):
    jsonld = graph.serialize(format="json-ld", context=context, encoding="utf-8")
    data_dict = json.loads(jsonld, object_pairs_hook=OrderedDict)
    data_dict.get('@graph').sort(key=lambda data: data["@id"])
    return data_dict


def write_graph(sorted_graph, data_type):
    out_file = open(f'../json-ld/{data_type}.json', 'w')
    json.dump(sorted_graph, out_file, indent=4)


def sort_and_write_graph_to_file(graph, context, data_type):
    sorted_graph = sort_graph(graph, context)
    write_graph(sorted_graph, data_type)
