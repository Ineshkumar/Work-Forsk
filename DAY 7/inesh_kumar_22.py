# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:31:45 2018

@author: inesh
"""

import oauth2
import time
import urllib2
import json

url1 = "https://api.twitter.com/1.1/search/tweets.json"  # FIXED AUTHENCATION PARAMETERS

params = {
        "oauth_version": "1.0",
        "oauth_nonce": oauth2.generate_nonce(),
        "oauth_timestamp": int(time.time())
    }

consumer = oauth2.Consumer(key="MOLSku6vv7wkDUHyQuKxSDE1h", secret="z3D9D28zW2BuhbcKqADCAN7fhXrbeBGPmm5MTC1lEsWPZCZq1v")

token = oauth2.Token(key="2791721754-UHbZSsJiHKjRRDG8gYQsJfekwyl1nniEopewm1j",
                     secret="J3AUIoGXuygrlrnF74EevMm92vB6KTI5aBkxHGhad4SmP")

params["oauth_consumer_key"] = consumer.key   # VARIABLE AUTHENCATION PARAMETERS

params["oauth_token"] = token.key
params["q"] = "jaipur"
req = oauth2.Request(method="GET", url=url1, parameters=params)

signature_method = oauth2.SignatureMethod_HMAC_SHA1() 
req.sign_request(signature_method, consumer, token)
url = req.to_url()
response = urllib2.Request(url)
data = urllib2.urlopen(response)
filename = params["q"]      
f = open(filename + "_File.txt", "w")  # SAVING DATA TO FILE
json.dump(data["statuses"], f)
f.close()

