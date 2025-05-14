# functions/fetcher.py

import requests
import csv
import datetime

def fetch_data(date_str: str):
    data = []
    API_URL = "自分で変更する"
    try:
        res = requests.get(API_URL)
        raw_data = csv.reader(res.text.strip().splitlines())
        for row in raw_data:
            if row[1]=='Ｒ３ー１Ｆ_ＥＨ':
                data.append(list(map(str,row[0:7])))
        return data
    except requests.exceptions.RequestException as e:
        return f"リクエストエラー: {e}"

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