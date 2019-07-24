#!/usr/bin/python3

import sys
import requests
import datetime
import pandas as pd
import io

def crawl_price(stock_id):
    now = int(datetime.datetime.now().timestamp())+86400
    url = "https://query1.finance.yahoo.com/v7/finance/download/" + stock_id + "?period1=0&period2=" + str(now) + "&interval=1d&events=history&crumb=hP2rOschxO0"
    response = requests.post(url)

    f = io.StringIO(response.text)
    df = pd.read_csv(f, index_col='Date', parse_dates=['Date'])
    return df

if __name__ == '__main__':
    print(sys.argv[1])
    print(crawl_price(sys.argv[1]))
