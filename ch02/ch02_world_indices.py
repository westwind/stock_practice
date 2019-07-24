#!/usr/bin/python3

import requests
import pandas as pd
import io

url = "https://finance.yahoo.com/world-indices/"
response = requests.get(url)

f = io.StringIO(response.text)
dfs = pd.read_html(f)
world_index = dfs[0]
print(world_index)
