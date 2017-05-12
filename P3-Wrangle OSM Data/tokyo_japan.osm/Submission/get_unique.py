# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import xml.etree.cElementTree as ET
from audit_osm import get_element
FILE = "tokyo_japan.xml"

NODE_FIELDS = ['id', 'lat', 'lon', 'user', 'uid', 'version', 'changeset', 'timestamp']
NODE_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_FIELDS = ['id', 'user', 'uid', 'version', 'changeset', 'timestamp']
WAY_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_NODES_FIELDS = ['id', 'node_id', 'position']

def get_unique(file, fields):
    unique = set()
    for element in get_element(file, tags=['node','way', 'relation']):
        tags = element.findall('tag')
        for tag in tags:
            if "cuisine" in tag.attrib['k']:
                print tag.attrib
        
#        
#        for k,v in element.attrib.items():                   
#            if k in fields:
#                unique.add(element.attrib[k])
    return len(unique)

def find_non_unique_fields(file, tag, fields = ['id']):
    all_fields = set()
    non_unique = set()
    for element in get_element(file, tags=tag):
        if element.tag == tag:
            a = element.attrib
            for field in fields:
                if a[field] not in all_fields:
                    all_fields.add(a[field])
                else:
                    non_unique.add(a[field])
    return all_fields

print get_unique(FILE, ["user"])