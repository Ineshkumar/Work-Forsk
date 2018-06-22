# -*- coding: utf-8 -*-
"""
Created on Tue May 22 17:52:59 2018

@author: inesh
"""

import urllib2
url="https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page1 = urllib2.urlopen(url)

from bs4 import BeautifulSoup

soup1 = BeautifulSoup(page1.content,"html.parser")
print(soup1.prettify())
#all_table=soup.find_all('table')

right_table=soup.find('table',class_='wikitable sortable plainrowheaders jquery-tablesorter')


A,B,C,D,E,F,G=[],[],[],[],[],[],[]

for row in right_table.find_all("tr"):
    cells = row.find_all('td')
    states=row.find_all('th')
    if len(cells)==6:
        A.append(cells[0].find(text=True))
        B.append(cells[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))
        
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_capital']=E
df['Former_capital']=G
print df
