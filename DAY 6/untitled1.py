# -*- coding: utf-8 -*-
"""
Created on Thu May 17 10:14:19 2018

@author: inesh
"""

import zlib
a='hello world'
b=zlib.compress(a)
c=zlib.decompress()




import urllib2
url="http:"
url +="?q="
resp=urllib2.urlopen(url)

print resp.read()



import request 

resp = request.get(url)

print resp.text