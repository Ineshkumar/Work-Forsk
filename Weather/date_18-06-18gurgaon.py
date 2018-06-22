# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 12:29:25 2018

@author: inesh
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 10:57:18 2018

@author: inesh
"""

import requests
page=requests.get('https://www.wunderground.com/history/airport/VIDP/2018/6/18/DailyHistory.html?req_city=New+Delhi&req_state=&req_statename=India&reqdb.zip=00000&reqdb.magic=45&reqdb.wmo=42181')

from bs4 import BeautifulSoup
soup=BeautifulSoup(page.content,'html.parser')

#div=soup.find('div',class_='observations_details')
div_date=soup.find_all('div',class_='daily-history-select')
h2=div_date[0].find('h2')


table=soup.find_all("table",class_='obs-table')
tbody=table[0].find('tbody')
tr=tbody.find_all('tr')
date=[]
A,B,C,D,E,F,G,H=[],[],[],[],[],[],[],[]
for i in tr:
    count=i.find_all('td')
    A.append(count[0].text.strip())
    B.append(count[1].text.strip().split()[0])
    C.append(count[2].text.strip().split()[0])
    D.append(count[3].text.strip().split()[0])
    E.append(count[4].text.strip().split('%')[0])
    F.append(count[5].text.strip().split()[0])
    G.append(count[6].text.strip().split()[0])
    H.append(count[8].text.strip().split()[0])
    
for i in range(len(A)):
    date.append(h2.text)
import pandas as pd
df=pd.DataFrame(date,columns=["Date"])
df["Time"]=A
df["Temp"]=B
df["Heat Index"]=C
df["Dew Point"]=D
df["Humidity"]=E
df["Pressure"]=F
df["Visibility"]=G
df["Wind Speed"]=H

df.to_csv('june_18.csv', index=False)
           