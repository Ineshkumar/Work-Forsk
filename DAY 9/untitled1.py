# -*- coding: utf-8 -*-
"""
Created on Tue May 22 18:51:51 2018

@author: inesh
"""

import requests

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
#show the status like 200 also use  page.status_code

#show content page.content

#page
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

#show the content in a particular manner
#print(soup.prettify())


#two tags at the top level of the page
list(soup.children)

#see type of each element 
[type(item) for item in list(soup.children)]

#other than the html and \n now we are taking an 3rd element with all nested tags
html = list(soup.children)[2]



#children in side 3rd tag
list(html.children)
body = list(html.children)[3]

#children inside body
list(body.children)



#children in side p
p = list(body.children)[1]

p.get_text()

