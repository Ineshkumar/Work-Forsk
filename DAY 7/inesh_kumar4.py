# -*- coding: utf-8 -*-
"""
Created on Sat May 19 13:03:08 2018

@author: inesh
"""
import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "MOLSku6vv7wkDUHyQuKxSDE1h",
    "consumer_secret"     : "z3D9D28zW2BuhbcKqADCAN7fhXrbeBGPmm5MTC1lEsWPZCZq1v",
    "access_token"        : "2791721754-UHbZSsJiHKjRRDG8gYQsJfekwyl1nniEopewm1j",
    "access_token_secret" : "J3AUIoGXuygrlrnF74EevMm92vB6KTI5aBkxHGhad4SmP" 
    }

  api = get_api(cfg)
  tweet = "python"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing
if __name__ == "__main__":
  main()
  
  
  