import numpy as np
import pandas as pd
import requests
from requests.exceptions import HTTPError
import typing as t

CRYPTOCURRENCY = "ethereum"     # change this for different cryptocurrencies
FILE_URL = f"./{CRYPTOCURRENCY}_api.csv"

def fetch_data() -> t.List :
    """
        - Fetch Data from API
        - Interval - d1 (daily)
        - Start - 1st Jan 2016
        - End - 12th Oct 2021
    """
    try:
        response = requests.get(f"https://api.coincap.io/v2/assets/{CRYPTOCURRENCY}/history", 
                        params={
                            "interval": "d1",
                            "start": "1451629800000",
                            "end": "1634020200000"
                        })
        response.raise_for_status()
        return response.json()["data"]
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

def save_data():
    data = fetch_data()
    df = pd.DataFrame(data)
    df.to_csv(FILE_URL)

if __name__ == "__main__":
    save_data()