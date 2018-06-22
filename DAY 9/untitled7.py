# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:43:53 2018

@author: inesh
"""

import urllib2
import unicodedata

hacker='https://www.livewireindia.com/article.php?title=Top_12_Indian_Ethical_Hacker_In_2017&id=40'
page=urllib2.urlopen(hacker)


from bs4 import BeautifulSoup

soup=BeautifulSoup(page)

allh=soup.findAll('div')

right_h3=soup.find('div',class_='container padding-top80 padding-bottom40')
A=[]

for i in right_h3.findAll("h3"):
    cells=i.findAll('strong')
    print cells[0]
    if not "u'\xa0'" in str(cells[0].text.strip()):
        print cells[0]
        A.append(str(cells[0].find(text=True)))
    else:
        
        print cells[0]
        unicodedata.normalize('NFKD', cells[0].text.strip()).encode('ascii','ignore')
        A.append(str(cells[0].find(text=True)))
        
        
    
    
import pandas as pd
df=pd.DataFrame(A,columns=['Name'])