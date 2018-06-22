# -*- coding: utf-8 -*-
"""
Created on Thu May 24 19:50:50 2018

@author: inesh
"""

from pandas import DataFrame
import mysql.connector

# connect to  MySQL server along with Database name
conn = mysql.connector.connect(user='root', password='ini773',
                              host='localhost',
                              database='job_satisfaction')

# Creating cursor Object from connection object
cursor = conn.cursor()

query = ("SELECT * FROM job_satisfaction;")  # query Database
cursor.execute(query)  # execute Query
df = DataFrame(cursor.fetchall())  # putting the result into Dataframe
df.columns = cursor.column_names  # Setting the Column names as it was in database.