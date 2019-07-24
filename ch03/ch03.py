#!/usr/bin/python3

import sys
import requests
import datetime
import pandas as pd
import io
import time

import pandas as pd
import matplotlib.pyplot as plt

def get_world_index_dict():
    world_index_dict = {}

    url = "https://finance.yahoo.com/world-indices/"
    response = requests.get(url)
    f = io.StringIO(response.text)
    dfs = pd.read_html(f)
    world_index = dfs[0]
    
    for symbol, name in zip(world_index['Symbol'], world_index['Name']):
        world_index_dict[name] = symbol
  
    return world_index_dict

def crawl_price(stock_id):
    now = int(datetime.datetime.now().timestamp())+86400
    url = "https://query1.finance.yahoo.com/v7/finance/download/" + stock_id + "?period1=0&period2=" + str(now) + "&interval=1d&events=history&crumb=hP2rOschxO0"
    response = requests.post(url)

    f = io.StringIO(response.text)
    df = pd.read_csv(f, index_col='Date', parse_dates=['Date'])
    return df

if __name__ == '__main__':
    index_dict = get_world_index_dict()
    world_index_history = {}
    for name in index_dict:
        print("Fetching " + name + "......")
        world_index_history[name] = crawl_price(index_dict[name])
        time.sleep(5)

    fig = plt.figure()
    for name, history in world_index_history.items():
        plt.plot(history.Close)
    fig.savefig('ch03.png')
