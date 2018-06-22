# -*- coding: utf-8 -*-
"""
Created on Fri May 25 18:36:23 2018

@author: inesh
"""

import urllib2
from bs4 import BeautifulSoup

page=urllib2.urlopen("https://www.livewireindia.com/article.php?title=Top_12_Indian_Ethical_Hacker_In_2017&id=40")

soup = BeautifulSoup(page.read(), 'html.parser')

#tags=soup.find('tbody')
#tags=soup.find('table')

tags=soup.find('div',class_="container padding-top80 padding-bottom40")

i=tags.find_all("h3")

A=[]

for Each_entry in i:
    A.append(Each_entry.text)

print A