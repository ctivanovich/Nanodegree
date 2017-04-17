# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:01:57 2017

@author: Christopher
"""

import sqlite3

path = "C:\\Users\\Christopher\\OneDrive\\Nanodegree\\P3-Wrangle Map Data\\chinook_db\\"

db = sqlite3.connect(path + "Chinook_Sqlite.sqlite")
c = db.cursor()

#How many unique customers have purchased a jazz track?
QUERY = """
SELECT G.Name, Count(*) FROM Genre as G
    JOIN Track as T on G.GenreId = T.GenreId
    JOIN (Select Avg(Milliseconds) as average from Track) as subq
    Where T.Milliseconds < average
    group by G.Name
    order by Count(*) desc
;"""
c.execute(QUERY)
rows = c.fetchall()

'''Uncomment to see your query in python'''
print("Number of entries:")
print(len(rows))

'''Uncomment to print your query by row'''
print("your output:")
for row in rows:
    print("  ", row[0:])

'''Uncomment to see your query as a pandas dataframe.
This is similar to the output you've been seeing throughout this course
You can learn more about pandas dataframes in our Intro to Data Analysis course!'''

#import pandas as pd
#df = pd.DataFrame(rows)
#print df

db.close()
