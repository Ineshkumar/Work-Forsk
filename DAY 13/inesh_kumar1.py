# -*- coding: utf-8 -*-
"""
Created on Mon May 28 11:37:31 2018

@author: inesh
"""
import urllib2
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

page=urllib2.urlopen("https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area")

soup = BeautifulSoup(page.read(), 'html.parser')

tags=soup.find('table', class_="wikitable")

A,B=[],[]

for row in tags.find_all("tr"):
    cells=row.find_all("td")
    if cells!=[]:
        A.append(str(cells[1].text.strip()))
        B.append(str(cells[4].text.strip()))

lst_top6=map(lambda x:float(x), B[:6])

explode=[]
        
for i in range(0,6):
    if(max(lst_top6)==lst_top6[i]):
        explode.append(0.2)
    else:
        explode.append(0)

plt.pie(B[:6],labels=A[:6],explode=explode)
plt.show()



    
