##
# @author Ma Joinna Anais Patiag 
 # @file Description
 # @desc Created on 2024-06-16 10:18:24 pm
 # @copyright APPI SASU
 #
"""
This project aims to create a predictive modelling using Animal Shelter data.
Objective: 
- Develop a model that would predict the likelihood of animal adoptability based on their chracteristic or breed.

"""

# Import Packages

import requests
from requests.auth import HTTPBasicAuth
import pandas as pd

# Amend in future developments to get real time Data
# Create variable for url and auth
# url = 'https://data.austintexas.gov/resource/9t4d-g238.json'
# client_id = '5p265t910xf7d0ze017oaxe45'
# client_secret = '4g1yjswhxny4ukhjlxejydkv9lh9956cs45k85f6bj2m0a0xi'
# token_url = 'https://api.socrata.com/oauth/token'

# # Prepare the data for the GET request
# data = {
#     'grant_type': 'client_credentials',
#     'client_id': client_id,
#     'client_secret': client_secret
# }

# response = requests.get(token_url, data=data)

# # Create a response for connection success or error
# if response.status_code == 200:
#     token_info = response.json()
#     access_token = token_info['access_token']
#     print(f"Access Token: {access_token}")
# else:
#     print(f"Failed to get access token: {response.status_code} {response.text}")

# Create a csv file variable
csv_file = pd.read_csv("/Users/joinna/Desktop/Projects/Projects/Personal_Projects/Austin_Animal_Center_Outcomes_20240616.csv")
df = pd.DataFrame(csv_file)

print(df)