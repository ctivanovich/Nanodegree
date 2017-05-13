# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:01:02 2017

@author: Christopher
"""

import xml.etree.cElementTree as ET
import os
import pprint as pt

ppt = pt.PrettyPrinter(indent=4)

path = os.getcwd()


xml = ET.parse(path+"\\osm.xml")

root = xml.getroot()

alltags = []

for event, element in ET.iterparse(path+"\\osm.xml"):
    if element.tag == "node":
        print (event, element.tag,element.attrib)
        alltags.append(element.findall("tag"))

ppt.pprint(alltags)

#for tag in tags:
#    print(tag.tag,tag.attrib)
#    for subtag in tag:
#        alltags.append(tag.attrib)
#print((alltags))