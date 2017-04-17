#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Please note that the function 'make_request' is provided for your reference only.
# You will not be able to to actually use it from within the Udacity web UI.
# Your task is to process the HTML using BeautifulSoup, extract the hidden
# form field values for "__EVENTVALIDATION" and "__VIEWSTATE" and set the appropriate
# values in the data dictionary.
# All your changes should be in the 'extract_data' function
from bs4 import BeautifulSoup
import requests
import json
import os

path = os.getcwd()
url = "https://www.transtats.bts.gov/Data_Elements.aspx?Data=2"
s = requests.Session()

def make_soup(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


"""What is being returned by our post request? A Json object? Check that, then figure out what you want to write to file with Write_Data"""
def post_request(header_values, carrier, airport):
    eventvalidation = header_values["eventvalidation"]
    viewstate = header_values["viewstate"]
    viewstategenerator = header_values["viewstategenerator"]
    r = s.post("https://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
           data = (
                   ("__EVENTTARGET", ""),
                   ("__EVENTARGUMENT", ""),
                   ("__VIEWSTATE", viewstate),
                   ("__VIEWSTATEGENERATOR",viewstategenerator),
                   ("__EVENTVALIDATION", eventvalidation),
                   ("CarrierList", carrier),
                   ("AirportList", airport),
                   ("Submit", "Submit")
                  ))
    return r.text

def extract_carriers(soup):
    data = []
    carrierlist = soup.find(id="CarrierList")
    for option in carrierlist.find_all("option"):
        carriercode = option["value"]
        if len(carriercode) < 3:
            data.append(carriercode)
    return data

def extract_airports(soup):
    data = []
    airports = soup.find(id="AirportList")
    for option in airports.find_all("option"):
        apcode = option["value"]
        if len(apcode) == 3 and "all" not in apcode.lower():
            data.append(apcode)
    return data

def extract_header_values(soup):
    header_values = {}
    fields = ["__EVENTVALIDATION",
              "__VIEWSTATE",
              "__VIEWSTATEGENERATOR"
             ]
    for field in fields:
        elval = soup.find(id=field)
        header_values[field[2:].lower()] = elval["value"]
    return header_values

def write_data(soup):
    header_values = extract_header_values(soup)
    airports = extract_airports(soup)
    carriers = extract_carriers(soup)
#    for airport, carrier in zip(carriers, airports):
    f = open(path+"\\{0}-{1}.html".format("AA","ORD"), "w")
    data = post_request(header_values, "AA", "ORD")
    f.write(data)
    f.close()
#        break
    return None

if __name__ == "__main__":
    html = make_soup(url)
    write_data(html)