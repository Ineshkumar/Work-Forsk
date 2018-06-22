# -*- coding: utf-8 -*-
"""
Created on Fri May 25 09:49:00 2018

@author: inesh
"""

import urllib2
from bs4 import BeautifulSoup

page=urllib2.urlopen("https://en.wikipedia.org/wiki/List_of_districts_of_Rajasthan")

soup = BeautifulSoup(page.read(), 'html.parser')

#tags=soup.find('tbody')
#tags=soup.find('table')

tags=soup.find('table',class_="wikitable sortable")

i=tags.find_all("tr")

A,B,C,D,E,F=[],[],[],[],[],[]

for s in range(len(i)):
    if(s!=0):
        cells=i[s].find_all('td')
        A.append(str(cells[0].text.strip()))
        B.append(str(cells[1].text.strip()))
        C.append(str(cells[2].text.strip()))
        D.append(str(cells[3].text.strip()))
        E.append(str(cells[4].text.strip()))
        F.append(str(cells[5].text.strip()))
        #F.append(cells[5].a['href'])

import pandas as pd
df=pd.DataFrame(A,columns=['District'])
df['Headquaters']=B
df['Area']=C
df['Population']=D
df['Division']=E
df['Url']=F
print df
