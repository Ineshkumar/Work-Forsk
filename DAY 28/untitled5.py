# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 12:05:08 2018

@author: inesh
"""

#Description:Car License plate detection of India
 #Author: Forsk Technologies
 #Version:1.1
 #Revision Date:27/08/2016


from havenondemand.hodclient import *
import json
import pandas as pd

client = HODClient("cb570dce-8951-4a71-898e-aae8c4d4f029", "v1") #apikey

#params = {'url': 'https://www.havenondemand.com/sample-content/videos/gb-plates.mp4', 'source_location': 'GB'} ##if using url
params = {'file': '/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 28/VID_20180619_122225(1)(1).mp4', 'source_location': 'IN'} ## or if using a local file
response_async = client.post_request(params, 'recognizelicenseplates', async=True)
jobID = response_async['jobID']
#print jobID

## Wait some time afterwards for async call to process...
response = client.get_job_result(jobID)
print response

#dump data in a json file
with open('data.json', 'w') as outfile:
    json.dump(response, outfile)
