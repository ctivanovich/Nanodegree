# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:16:57 2017

@author: Christopher
"""


import csv
import codecs
import pprint
import re
import xml.etree.cElementTree as ET

import cerberus

import schema

import audit_osm as ao

OSM_PATH = "tokyo_center.osm"

NODES_PATH = "nodes.csv"
NODE_TAGS_PATH = "nodes_tags.csv"
WAYS_PATH = "ways.csv"
WAY_NODES_PATH = "ways_nodes.csv"
WAY_TAGS_PATH = "ways_tags.csv"

LOWER_COLON = re.compile(r'^([a-z]|_)+:([a-z]|_)+')
PROBLEMCHARS = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

SCHEMA = schema.Schema

# Make sure the fields order in the csvs matches the column order in the sql table schema
NODE_FIELDS = ['id', 'lat', 'lon', 'user', 'uid', 'version', 'changeset', 'timestamp']
NODE_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_FIELDS = ['id', 'user', 'uid', 'version', 'changeset', 'timestamp']
WAY_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_NODES_FIELDS = ['id', 'node_id', 'position']


def shape_element(element, node_attr_fields=NODE_FIELDS, way_attr_fields=WAY_FIELDS,
                  problem_chars=PROBLEMCHARS, default_tag_type='regular'):
    """Clean and shape node or way XML element to Python dict"""

    node_attribs = {}
    way_attribs = {}
    way_nodes = []
    tags = []  # Handle secondary tags the same way for both node and way elements

    # YOUR CODE HERE
    if element.tag == 'node':
        node = element.attrib
        node_attribs = {k:v for k, v in node.items() if k in node_attr_fields}

        node_tags = element.findall("tag")
        for elem in node_tags:
            elem = elem.attrib
            k = elem['k']
            if PROBLEMCHARS.search(k):
                continue
            if ":" in k: 
                colpos = k.find(":")
                k = k[colpos+1:]
            id = node['id'] #parent Node's id
            v = elem['v']
            if 'name' in k:
                ttype = "name"
                k = ao.langtype(v)
            elif 'cuisine:' in elem['k']:
                v = 'japanese' if elem['k'][colpos+1:] == 'ja' else elem['k'][colpos+1:]
                k = 'cuisine'
                ttype = "regular"
            else:
                ttype = default_tag_type if ":" not in elem['k'] else elem['k'][:colpos]
            tags.append({'id':id, 'key':k, 'value':v, 'type':ttype})
        return {'node': node_attribs, 'node_tags': tags}
    elif element.tag == 'way':
        way = element.attrib
        way_attribs = {k:v for k, v in way.items() if k in way_attr_fields}
        ###Handling the way tags
        way_tags = element.findall("tag")
        for elem in way_tags:
            elem = elem.attrib
            k = elem['k']
            if PROBLEMCHARS.search(k):
                continue
            if ":" in k: 
                colpos = k.find(":")
                k = k[colpos+1:]
            id = way['id'] #parent Node's id
            v = elem['v']
            if 'name' in k:
                ttype = "name"
                k = ao.langtype(v)
            elif 'cuisine:' in elem['k']:
                v = 'japanese' if elem['k'][colpos+1:] == 'ja' else elem['k'][colpos+1:]
                k = 'cuisine'
                ttype = "regular"
            else:
                ttype = default_tag_type if ":" not in elem['k'] else elem['k'][:colpos]
            tags.append({'id':id, 'key':k, 'value':v, 'type':ttype})

        ###Handling the way nodes
        all_way_nodes = element.findall("nd")
        for i, el in enumerate(all_way_nodes):
            way_nodes.append({'id':way['id'], 'node_id':el.attrib['ref'], 'position':i})
        # pprint.pprint(all_way_nodes)

        return {'way': way_attribs, 'way_nodes': way_nodes, 'way_tags': tags}


# ================================================== #
#               Helper Functions                     #
# ================================================== #
def get_element(osm_file, tags=('node', 'way', 'relation')):
    """Yield element if it is the right type of tag"""

    context = ET.iterparse(osm_file, events=('start', 'end'))
    _, root = next(context)
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            yield elem
            root.clear()


def validate_element(element, validator, schema=SCHEMA):
    """Raise ValidationError if element does not match schema"""
    if validator.validate(element, schema) is not True:
        field, errors = next(validator.errors.iteritems())
        message_string = "\nElement of type '{0}' has the following errors:\n{1}"
        error_string = pprint.pformat(errors)

        raise Exception(message_string.format(field, error_string))


class UnicodeDictWriter(csv.DictWriter, object):
    """Extend csv.DictWriter to handle Unicode input"""

    def writerow(self, row):
        super(UnicodeDictWriter, self).writerow({
            k: (v.encode('utf-8') if isinstance(v, unicode) else v) for k, v in row.iteritems()
        })

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


# ================================================== #
#               Main Function                        #
# ================================================== #
def process_map(file_in, validate):
    """Iteratively process each XML element and write to csv(s)"""

    with codecs.open(NODES_PATH, 'wb') as nodes_file, \
         codecs.open(NODE_TAGS_PATH, 'wb') as nodes_tags_file, \
         codecs.open(WAYS_PATH, 'wb') as ways_file, \
         codecs.open(WAY_NODES_PATH, 'wb') as way_nodes_file, \
         codecs.open(WAY_TAGS_PATH, 'wb') as way_tags_file:

        nodes_writer = UnicodeDictWriter(nodes_file, NODE_FIELDS)
        node_tags_writer = UnicodeDictWriter(nodes_tags_file, NODE_TAGS_FIELDS)
        ways_writer = UnicodeDictWriter(ways_file, WAY_FIELDS)
        way_nodes_writer = UnicodeDictWriter(way_nodes_file, WAY_NODES_FIELDS)
        way_tags_writer = UnicodeDictWriter(way_tags_file, WAY_TAGS_FIELDS)

        nodes_writer.writeheader()
        node_tags_writer.writeheader()
        ways_writer.writeheader()
        way_nodes_writer.writeheader()
        way_tags_writer.writeheader()

        validator = cerberus.Validator()

        for element in get_element(file_in, tags=('node', 'way')):
            el = shape_element(element)
            if el:
                if validate is True:
                    validate_element(el, validator)

                if element.tag == 'node':
                    nodes_writer.writerow(el['node'])
                    node_tags_writer.writerows(el['node_tags'])
                elif element.tag == 'way':
                    ways_writer.writerow(el['way'])
                    way_nodes_writer.writerows(el['way_nodes'])
                    way_tags_writer.writerows(el['way_tags'])


if __name__ == '__main__':
    # Note: Validation is ~ 10X slower. For the project consider using a small
    # sample of the map when validating.
    process_map(OSM_PATH, validate=False)