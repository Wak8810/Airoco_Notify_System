from functions.fetcher import fetch_data
from functions.fetcher import get_period_data
import time

def main():
    curr_time = int(time.time())
    tt = curr_time - 60 * 60 * 12
    date_str = str(tt)
    data = fetch_data(date_str)
    period_data = get_period_data(data)
    for i in period_data[0]:
        print(i)


if __name__ == "__main__":
    main()