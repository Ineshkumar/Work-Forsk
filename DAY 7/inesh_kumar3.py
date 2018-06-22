# -*- coding: utf-8 -*-
"""
Created on Fri May 18 21:28:07 2018

@author: inesh
"""



import facebook as fb 
import os
# Facebook Graphic Explorer API user Access Token
access_token = "EAACEdEose0cBAEhF08wi6SAE1I5ZBsABynuAqNVkT2GruvBn7oMsZATg2ZAKbuAYcxzWnCISkYkLjxWKcRKTzAaIL7dPl4doDkDtfTUNoObyDLcTPAwsxcf3ZCfAhZAvQwlGTJKdYtvvdWrOOoQTV3tHSZAVgCLOwRZBbNiW65uDFqpRivBviX0MtSNLcZC2ZAnFZBPNSCQaBflQZDZD"

# Message to post as status on Facebook
#status = "<done with python>"

# Authenticating
graph = fb.GraphAPI(access_token)
# Posting Status on your wall



post_id = graph.put_photo(image=open('/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY7/whatcountsas.jpg','rb'),message='again python')


