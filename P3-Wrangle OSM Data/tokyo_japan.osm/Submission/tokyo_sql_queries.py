# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:01:57 2017

@author: Christopher
"""

import sqlite3

path = "C:\\Users\\Christopher\\OneDrive\\Nanodegree\\P3-Wrangle OSM Data\\tokyo_japan.osm\\"

db = sqlite3.connect(path + "tokyofull.db")
c = db.cursor()

#How many unique customers have purchased a jazz track?
query1 = """
SELECT e.user, COUNT(*) as num
FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e
GROUP BY e.user
ORDER BY num DESC
LIMIT 10
;"""

query2 = '''
SELECT value, count(*) as num
FROM ways_tags
WHERE key = "amenity"
GROUP BY value
ORDER BY num DESC
LIMIT 10
;'''

query3 = '''
SELECT n.user, count(*)
FROM nodes AS n JOIN ways_tags AS nt ON n.id = nt.id
WHERE n.user = "futurumspes" OR n.user = "Tom_G3X" OR n.user = "Ryo-a"
GROUP BY n.user
;'''

c.execute(query3)
rows = c.fetchall()


entries_by_year = {}
for year in range(2007,2018):
    query4 = '''
    select count(timestamp)
    from nodes
    where timestamp LIKE "{0}%"
    ;'''.format(str(year))
    c.execute(query4)
    rows = c.fetchall()
    entries_by_year[year] = rows[0][0]

import pandas as pd
df = pd.DataFrame(rows)
print df

db.close()
