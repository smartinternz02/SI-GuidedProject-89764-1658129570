# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 18:54:41 2022

@author: vadla
"""

import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "cKm81MU-WUjmdSQmhsHhL43v6ZI5VDH8lo6AFJbeDd3A"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["blood_urea","blood glucose random","anemia","coronary_artery_disease","pus_cell","red_blood_cells","diabetesemellitus","pedal_edema"]], "values": [[17.0,102.000000,0,0,1,1,1,0]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/3d42cf89-772b-4bc2-a87d-22e7f5559234/predictions?version=2022-08-02', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions = response_scoring.json()
pred = predictions['predictions'][0]['values'][0][0]
if (pred == 0):
    print("you have kidney disease")
else:
    print("you don't have any kidney disease")