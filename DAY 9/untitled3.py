# -*- coding: utf-8 -*-
"""
Created on Fri May 25 09:12:58 2018

@author: inesh
"""

import requests

page = requests.get("https://en.wikipedia.org/wiki/List_of_districts_of_Rajasthan")

#page.status_code

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.read(), 'lxal')


#right_table=soup.find('table',class_='wikitable sortable jquery-tablesorter')

right_tables=soup.find('tbody')


A,B,C,D,E,F=[],[],[],[],[],[]

for row in right_tables.findAll("tr"):
    cells = row.find_all('td')
    A.append(str(cells[0].text.strip()))
    B.append(str(cells[1].text.strip()))
    C.append(str(cells[2].text.strip()))
    D.append(str(cells[3].text.strip()))
    E.append(str(cells[4].text.strip()))
    F.append(str(cells[5].text.strip()))
        
import pandas as pd
df=pd.DataFrame(A,columns=['District'])
df['Headquaters']=B
df['Area']=C
df['Population']=D
df['Division']=E
df['Url']=E
print df
