from functions.fetcher import fetch_data
from functions.fetcher import get_period_data
from functions.send_notify import send_slack_message
from functions.make_message import make_message
from functions.calc_average import get_ave
from functions.calc_score import get_period_scores
import sys
import os

# プロジェクトのルートディレクトリをPythonパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.add_scores import add_scores
import time
from datetime import datetime

def main():
    curr_time = int(time.time())
    tt = curr_time - 60 * 60 * 12
    date_str = str(tt)
    # 日付をYYYY-MM-DD形式に変換
    current_date = datetime.fromtimestamp(tt).strftime('%Y-%m-%d')
    
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

    print(r3_301_period_elements)
    r3_301_period_scores = get_period_scores(r3_301_period_elements)
    r3_401_period_scores = get_period_scores(r3_401_period_elements)
    r3_403_period_scores = get_period_scores(r3_403_period_elements)
    print(r3_301_period_scores)

    _301_text = make_message(r3_301_period_scores, 0)
    _401_text = make_message(r3_401_period_scores, 1)
    _403_text = make_message(r3_403_period_scores, 2)
    print(_301_text)
    print(_401_text)
    print(_403_text)
    """
    send_slack_message(_301_text)
    send_slack_message(_401_text)
    send_slack_message(_403_text)
    """

    # データベースにスコアを追加
    for period in range(6):
        # R3-301のスコアを追加
        if period < len(r3_301_period_scores) and r3_301_period_scores[period] is not None:
            add_scores(
                classroom_name="R3-301",
                date=current_date,
                period=period + 1,
                co2_score=r3_301_period_scores[period][0],
                temp_score=r3_301_period_scores[period][1],
                humi_score=r3_301_period_scores[period][2]
            )
        
        # R3-401のスコアを追加
        if period < len(r3_401_period_scores) and r3_401_period_scores[period] is not None:
            add_scores(
                classroom_name="R3-401",
                date=current_date,
                period=period + 1,
                co2_score=r3_401_period_scores[period][0],
                temp_score=r3_401_period_scores[period][1],
                humi_score=r3_401_period_scores[period][2]
            )
        
        # R3-403のスコアを追加
        if period < len(r3_403_period_scores) and r3_403_period_scores[period] is not None:
            add_scores(
                classroom_name="R3-403",
                date=current_date,
                period=period + 1,
                co2_score=r3_403_period_scores[period][0],
                temp_score=r3_403_period_scores[period][1],
                humi_score=r3_403_period_scores[period][2]
            )

if __name__ == "__main__":
    main()