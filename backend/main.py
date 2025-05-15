from functions.fetcher import fetch_data
from functions.fetcher import get_period_data
from functions.send_notify import send_slack_message
from functions.make_message import make_message
from functions.calc_average import get_ave
from functions.calc_score import get_period_scores
import time

def main():
    curr_time = int(time.time())
    tt = curr_time - 60 * 60 * 12
    date_str = str(tt)
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
    
    send_slack_message(_301_text)
    send_slack_message(_401_text)
    send_slack_message(_403_text)

if __name__ == "__main__":
    main()