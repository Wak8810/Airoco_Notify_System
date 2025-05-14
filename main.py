from functions.fetcher import fetch_data
from functions.fetcher import get_period_data
from functions.calc_score import get_co2_score
from functions.calc_score import get_low_temp_score
from functions.calc_score import get_high_temp_score
from functions.calc_score import get_low_humi_score
from functions.calc_score import get_high_humi_score
from functions.fetcher import get_weekday
from functions.send_notify import send_slack_message
from functions.calc_average import get_ave
import time

def main():
    curr_time = int(time.time())
    tt = curr_time - 60 * 60 * 12
    date_str = str(tt)
    data = fetch_data(date_str, 2)
    period_data = get_period_data(data)
    period_elements = []
    for i in range(6):
        period_elements.append(get_ave(period_data[i]))
    print(period_elements)
    """
    for i in period_data[2]:
        print(i)

    for ele in period_data[2]:
        print("weekday:{} CO2:{} low_temp:{} high_temp:{} low_humi:{} high_humi:{}".format(get_weekday(ele), get_co2_score(ele), 
                                                                                get_low_temp_score(ele),
                                                                                get_high_temp_score(ele), 
                                                                                get_low_humi_score(ele), 
                                                                                get_high_humi_score(ele),))
                                                                """
        
if __name__ == "__main__":
    main()