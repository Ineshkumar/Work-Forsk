# -*- coding: utf-8 -*-
"""
Created on Tue May 22 12:32:45 2018

@author: inesh
"""

import urllib2

rank="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

page=urllib2.urlopen(rank)

from bs4 import BeautifulSoup

soup=BeautifulSoup(page)


right_tables=soup.find('tbody')

#list
A=[]
B=[]
C=[]
D=[]
E=[]

for row in right_tables.find_all("tr"):
    cells=row.find_all('td')
    A.append(str(cells[0].text.strip()))
    B.append(str(cells[1].text.strip()))
    C.append(str(cells[2].text.strip()))
    D.append(str(cells[3].text.strip()))
    E.append(str(cells[4].text.strip()))

import pandas as pd
df=pd.DataFrame(A,columns=['pos'])
df['Team']=B
df['Matches']=C
df['Points']=D
df['Ranking']=E
print df


