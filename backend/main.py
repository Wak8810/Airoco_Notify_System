from functions.fetcher import fetch_data
from functions.fetcher import get_period_data
from functions.send_notify import send_slack_message
from functions.make_message import make_message
from functions.calc_average import get_ave
from functions.calc_score import get_period_scores
import sys
import os
from datetime import datetime, timezone, timedelta

# プロジェクトのルートディレクトリをPythonパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.add_datas import add_datas
import time

def main():
    # 現在時刻をJSTで取得
    jst = timezone(timedelta(hours=+9))
    curr_time = datetime.now(jst)
    # 12時間前の時刻を取得
    tt = curr_time - timedelta(hours=12)
    date_str = str(int(tt.timestamp()))
    current_date = tt.strftime('%Y/%m/%d')
    
    r3_301_data = fetch_data(date_str, 0)
    r3_401_data = fetch_data(date_str, 1)
    r3_403_data = fetch_data(date_str, 2)
    r3_301_period_data = get_period_data(r3_301_data)
    r3_401_period_data = get_period_data(r3_401_data)
    r3_403_period_data = get_period_data(r3_403_data)
    r3_301_period_elements = []
    for i in range(6):
        r3_301_period_elements.append(get_ave(r3_301_period_data[i]))

    r3_401_period_elements = []
    for i in range(6):
        r3_401_period_elements.append(get_ave(r3_401_period_data[i]))
    
    r3_403_period_elements = []
    for i in range(6):
        r3_403_period_elements.append(get_ave(r3_403_period_data[i]))

    #print(r3_301_period_elements)
    r3_301_period_scores = get_period_scores(r3_301_period_elements)
    r3_401_period_scores = get_period_scores(r3_401_period_elements)
    r3_403_period_scores = get_period_scores(r3_403_period_elements)
    #print(r3_301_period_scores)

    texts_list = []
    classroom_nums = [301, 401, 403]
    texts_list.append(make_message(r3_301_period_scores, 0, current_date))
    texts_list.append(make_message(r3_401_period_scores, 1, current_date))
    texts_list.append(make_message(r3_403_period_scores, 2, current_date))
    
    for i in range(3):
        send_slack_message(texts_list[i],classroom_nums[i])

    # データベースにスコアを追加
    for period in range(6):
        # R3-301のスコアを追加
        if period < len(r3_301_period_scores) and r3_301_period_scores[period] is not None:
            add_datas(
                classroom_name="R3-301",
                date=tt.strftime('%Y-%m-%d'),  # データベース用はハイフン区切りのまま
                period=period + 1,
                co2_score=r3_301_period_scores[period][0],
                temp_score=min(r3_301_period_scores[period][1], r3_301_period_scores[period][2]),
                humi_score=min(r3_301_period_scores[period][3], r3_301_period_scores[period][4]),
                co2_value=r3_301_period_elements[period][5],
                temp_value=r3_301_period_elements[period][6],
                humi_value=r3_301_period_elements[period][7]
            )
        
        # R3-401のスコアを追加
        if period < len(r3_401_period_scores) and r3_401_period_scores[period] is not None:
            add_datas(
                classroom_name="R3-401",
                date=tt.strftime('%Y-%m-%d'),  # データベース用はハイフン区切りのまま
                period=period + 1,
                co2_score=r3_401_period_scores[period][0],
                temp_score=min(r3_401_period_scores[period][1], r3_401_period_scores[period][2]),
                humi_score=min(r3_401_period_scores[period][3], r3_401_period_scores[period][4]),
                co2_value=r3_401_period_elements[period][5],
                temp_value=r3_401_period_elements[period][6],
                humi_value=r3_401_period_elements[period][7]
            )
        
        # R3-403のスコアを追加
        if period < len(r3_403_period_scores) and r3_403_period_scores[period] is not None:
            add_datas(
                classroom_name="R3-403",
                date=tt.strftime('%Y-%m-%d'),  # データベース用はハイフン区切りのまま
                period=period + 1,
                co2_score=r3_403_period_scores[period][0],
                temp_score=min(r3_403_period_scores[period][1], r3_403_period_scores[period][2]),
                humi_score=min(r3_403_period_scores[period][3], r3_403_period_scores[period][4]),
                co2_value=r3_403_period_elements[period][5],
                temp_value=r3_403_period_elements[period][6],
                humi_value=r3_403_period_elements[period][7]
            )

if __name__ == "__main__":
    main()