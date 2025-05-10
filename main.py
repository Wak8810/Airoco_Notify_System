from functions.fetcher import fetch_data
from functions.fetcher import get_period_data
from functions.calc_score import get_co2_score
from functions.calc_score import get_low_temp_score
from functions.calc_score import get_high_temp_score
from functions.calc_score import get_low_humi_score
from functions.calc_score import get_high_humi_score
from functions.calc_score import get_total_score
import time

def main():
    curr_time = int(time.time())
    tt = curr_time - 60 * 60 * 12
    date_str = str(tt)
    data = fetch_data(date_str)
    period_data = get_period_data(data)
    for i in period_data[5]:
        print(i)

    for ele in period_data[5]:
        print("CO2:{} low_temp:{} high_temp:{} low_humi:{} high_humi:{} total:{}".format(get_co2_score(ele), 
                                                                                get_low_temp_score(ele),
                                                                                get_high_temp_score(ele), 
                                                                                get_low_humi_score(ele), 
                                                                                get_high_humi_score(ele),
                                                                                get_total_score(ele)))
        
if __name__ == "__main__":
    main()