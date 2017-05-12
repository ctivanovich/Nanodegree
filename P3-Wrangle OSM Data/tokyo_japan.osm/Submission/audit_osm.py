# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 10:23:57 2017

@author: Christopher
"""

import codecs
import xml.etree.cElementTree as ET
import csv
import data
from langdetect import detect
import pprint

OSM = 'tokyo_japan.xml'
SAMPLE = 'tokyo_extract.xml'
OUTFILE = 'unique_user_contributions.csv'

def get_element(osm_file, tags=('node', 'way', 'relation')):
    """Yield element if it is the right type of tag

    Reference:
    http://stackoverflow.com/questions/3095434/inserting-newlines-in-xml-file-generated-via-xml-etree-elementtree-in-python
    """
    context = iter(ET.iterparse(osm_file, events=('start', 'end')))
    _, root = next(context)
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            yield elem
            root.clear()

def langtype(v):
    try:
        lang = detect(unicode(v)[0])
        return lang
    except:
        return v

def is_cuisine(key):
    if "cuisine" in key:
        return True
    else:
        return False

def get_user_contributions(filename):
    contributions = {}
    for element in get_element(filename): #elems are Node, Way, or Relation entries
        ###get set of unique users
        attribute = element.attrib
        user = attribute["uid"]
        if 'uid' in element.attrib:
            user = get_user(element)
            contributions[user] = contributions.get(user, 0) + 1
    return contributions

def csv_writer(outfile, headers, data):
    with codecs.open(outfile, 'w') as f:
        w = csv.writer(f, delimiter=",", lineterminator='\n')
        w.writerow(headers)
        for entry in output:
            w.writerow(entry)

if __name__ == "__main__":
    output = get_user_contributions(SAMPLE)
    output = sorted(output.items(), key=lambda x:x[1])
    output.reverse()
    
#    csv_writer(OUTFILE, ["User ID", "Contributions"], output)
#    pp = pprint.PrettyPrinter(indent=4)
#    pp.pprint(output[:10])
