from urllib import response
import pandas as pd
import requests

download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"

response = requests.get(download_url)

response.status_code

with open('nba_all_elo.csv', 'wb') as f:
    f.write(response.content)

