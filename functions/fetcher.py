# functions/fetcher.py

import os
from dotenv import load_dotenv
import requests
import csv
import datetime

load_dotenv()

def fetch_data(date_str: str, cl_num: int):
    base_url = os.getenv('AIROCO_API_BASE_URL')
    sensor_id = os.getenv('AIROCO_ID')
    api_key = os.getenv('AIROCO_API_KEY')
    data = []
    API_URL = f"{base_url}?id={sensor_id}&subscription-key={api_key}&startDate={date_str}"
    classroom = ['Ｒ３ー３０１', 'Ｒ３ー４０１', 'Ｒ３ー４０３']
    try:
        res = requests.get(API_URL)
        raw_data = csv.reader(res.text.strip().splitlines())
        for row in raw_data:
            if row[1]==classroom[cl_num]:
                data.append(list(map(str,row[0:7])))
        return data
    except requests.exceptions.RequestException as e:
        return f"リクエストエラー: {e}"

def get_weekday(data: list):
    data = datetime.datetime.strptime(data[0], '%Y/%m/%d %H:%M:%S')
    return data.weekday()

def get_period_data(data: list):
    period_data = []
    period_data.append(get_first_period(data))
    period_data.append(get_second_period(data))
    period_data.append(get_third_period(data))
    period_data.append(get_fourth_period(data))
    period_data.append(get_fifth_period(data))
    period_data.append(get_sixth_period(data))
    return period_data

def get_first_period(data: list):
    start = datetime.time(9, 10)
    finish = datetime.time(10, 40)
    new_data = []

    for ele in data:
        tdatetime = datetime.datetime.strptime(ele[0], '%Y/%m/%d %H:%M:%S').time()
        if start <= tdatetime and tdatetime <= finish:
            new_data.append(ele)
    return new_data

def get_second_period(data: list):
    start = datetime.time(10, 50)
    finish = datetime.time(12, 20)
    new_data = []

    for ele in data:
        tdatetime = datetime.datetime.strptime(ele[0], '%Y/%m/%d %H:%M:%S').time()
        if start <= tdatetime and tdatetime <= finish:
            new_data.append(ele)
    return new_data

def get_third_period(data: list):
    start = datetime.time(13, 10)
    finish = datetime.time(14, 40)
    new_data = []

    for ele in data:
        tdatetime = datetime.datetime.strptime(ele[0], '%Y/%m/%d %H:%M:%S').time()
        if start <= tdatetime and tdatetime <= finish:
            new_data.append(ele)
    return new_data

def get_fourth_period(data: list):
    start = datetime.time(14, 50)
    finish = datetime.time(16, 20)
    new_data = []

    for ele in data:
        tdatetime = datetime.datetime.strptime(ele[0], '%Y/%m/%d %H:%M:%S').time()
        if start <= tdatetime and tdatetime <= finish:
            new_data.append(ele)
    return new_data

def get_fifth_period(data: list):
    start = datetime.time(16, 30)
    finish = datetime.time(18, 0)
    new_data = []

    for ele in data:
        tdatetime = datetime.datetime.strptime(ele[0], '%Y/%m/%d %H:%M:%S').time()
        if start <= tdatetime and tdatetime <= finish:
            new_data.append(ele)
    return new_data

def get_sixth_period(data: list):
    start = datetime.time(18, 10)
    finish = datetime.time(19, 40)
    new_data = []

    for ele in data:
        tdatetime = datetime.datetime.strptime(ele[0], '%Y/%m/%d %H:%M:%S').time()
        if start <= tdatetime and tdatetime <= finish:
            new_data.append(ele)
    return new_data