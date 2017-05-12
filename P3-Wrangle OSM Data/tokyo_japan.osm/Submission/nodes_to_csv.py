# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 15:20:22 2017

@author: Christopher
"""
import audit_osm as ao
import codecs
import csv
#import unicode

OSMFILE = 'tokyo_japan.xml'
NODESFILE = "tokyo_nodes.csv"
WAYSFILE = ''
TAGSFILE = ''



node_fields = ["id", "lat", "lon", "user", "uid", "version", "changeset", "timestamp"]

def get_nodes(osmfile):
    for element in ao.get_element(osmfile):
        if element.tag == "node":
            node_attr = element.attrib
            yield {key:value for key, value in node_attr.items() if key in node_fields}

def elements_to_csv(outfile):
    with codecs.open(outfile, 'w', encoding = "utf-8") as f:
        w = csv.DictWriter(f, node_fields, restval="NULL")
        w.writeheader()
        for node in get_nodes(OSMFILE):
            w.writerow(node)


if __name__ == "__main__":
    elements_to_csv(NODESFILE)