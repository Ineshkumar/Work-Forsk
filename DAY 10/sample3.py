# -*- coding: utf-8 -*-
"""
Created on Thu May 24 19:41:59 2018

@author: inesh
"""

import sqlalchemy
from pandas import DataFrame

engine = sqlalchemy.create_engine('mysql://root:@localhost/data science')
query = "select * from job_satisfaction"
resoverall = engine.execute(query)
df = DataFrame(resoverall.fetchall())
df.columns = resoverall.keys()