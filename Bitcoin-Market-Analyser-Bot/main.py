import requests
import sys
import os
import time
from datetime import datetime

Api_url = 'https://api.coinmarketcap.com/v1/ticker/'

if sys.platform.lower() == "win32":
    os.system('color')


class style():
    @staticmethod
    def RED(x): return '\033[31m' + str(x)
    @staticmethod
    def GREEN(x): return '\033[32m' + str(x)
    @staticmethod
    def YELLOW(x): return '\033[33m' + str(x)
    @staticmethod
    def RESET(x): return '\033[0m' + str(x)


def main():
    Price_At_start = requests.get(Api_url + 'bitcoin').json()[0]['price_usd']
    Lowest_Today = Price_At_start
    Highest_Today = Price_At_start
    Highest_time = ''
    Lowest_time = ''
    last_price = 0
    update = input("Update Rate In Seconds: ")
    update = int(update)
    while True:
        try:
            response = requests.get(Api_url + 'bitcoin')
            response_json = response.json()
            price = response_json[0]['price_usd']
            now = datetime.now()
            if price != last_price:
                print(now.strftime('%Y-%m-%d %H:%M:%S / ') +
                      style.GREEN("Price Changed") + style.RESET(""))
                if price <= str(last_price):
                    print(now.strftime('%Y-%m-%d %H:%M:%S') +
                          ' / Bitcoin price = ' + style.YELLOW(price) + style.RESET("") + ' USD / ' + style.RED(" Decrease") + style.RESET(""))
                else:
                    print(now.strftime('%Y-%m-%d %H:%M:%S') +
                          ' / Bitcoin price = ' + style.YELLOW(price) + style.RESET("") + ' USD / ' + style.GREEN(" Increase") + style.RESET(""))
                if str(Lowest_Today) > price:
                    Lowest_Today = price
                    Lowest_time = str(now.strftime('(%Y-%m-%d %H:%M:%S) '))
                if price > str(Highest_Today):
                    Highest_Today = price
                    Highest_time = str(now.strftime('(%Y-%m-%d %H:%M:%S)'))
                last_price = price
            time.sleep(update)
        except KeyboardInterrupt:
            print("Lowest Today: " + Lowest_time + Lowest_Today +
                  "\n" + "Highest Today: " + Highest_time + Highest_Today)
            quit()
        except:
            print(now.strftime('%Y-%m-%d %H:%M:%S / ') +
                  "Internet connection not detected.")
            time.sleep(update)


if __name__ == "__main__":
    main()
