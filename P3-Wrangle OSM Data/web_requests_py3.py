# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 12:52:07 2017

@author: Christopher
"""

import requests
import json
import codecs

URL_MAIN = "http://api.nytimes.com/svc/"
article_url = "api.nytimes.com/svc/search/v2/articlesearch.json"
URL_POPULAR = URL_MAIN + "mostpopular/v2/"
API_KEY = { "popular": "70cecfebab1e498daac44831bc8f86be",
            "article": "70cecfebab1e498daac44831bc8f86be"}

def query_site(url, target, offset):
    params = {"api-key": API_KEY[target], "offset": offset}
    r = requests.get(url, params = params)

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()
data = query_site(URL_POPULAR, "popular", 20)