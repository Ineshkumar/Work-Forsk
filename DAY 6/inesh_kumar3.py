# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:55:51 2018

@author: inesh
"""

# importing the requests library
import requests
import json
 
# defining the api-endpoint 
API_ENDPOINT = "http://13.127.155.43/api_v0.1/sending"
 
 
d={
	"Phone_Number": "7737732124",
	"Name": "inesh kumar",
	"College_Name": "skit",
	"Branch": "cse"
} 
headers={'Content-type':'application/json'}
# sending post request and saving response as response object
r = requests.post(API_ENDPOINT, data=json.dumps(d),headers=headers)
 
# extracting response text 
print r.text



import requests
 
# api-endpoint
URL = "http://13.127.155.43/api_v0.1/receiving?Phone_Number=7737732124"
 
# sending get request and saving the response as response object
r = requests.get(URL)
 
# extracting data in json format
print r.text