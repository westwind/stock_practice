#!/usr/bin/python3

import requests

site = "https://query1.finance.yahoo.com/v7/finance/download/2330.TW?period1=0&period2=1563858569&interval=1d&events=history&crumb=hP2rOschxO0"
response = requests.post(site)

with open('ch01.csv', 'w') as f:
    f.writelines(response.text)
