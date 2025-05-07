# functions/fetcher.py

import requests
import time
import csv

def fetch_data(date_str: str):
    data = []
    API_URL = f'https://airoco.necolico.jp/data-api/day-csv?id=CgETViZ2&subscription-key=6b8aa7133ece423c836c38af01c59880&startDate={date_str}'
    try:
        res = requests.get(API_URL)
        raw_data = csv.reader(res.text.strip().splitlines())
        for row in raw_data:
            if row[1]=='Ｒ３ー１Ｆ_ＥＨ':
                data.append(list(map(str,row[0:7])))
        return data
    except requests.exceptions.RequestException as e:
        return f"リクエストエラー: {e}"
