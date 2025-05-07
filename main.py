from functions.fetcher import fetch_data
import time

def main():
    curr_time = int(time.time())
    tt = curr_time - 60 * 60 * 12
    date_str = str(tt)
    data = fetch_data(date_str)
    for i in data:
        print(i)

if __name__ == "__main__":
    main()