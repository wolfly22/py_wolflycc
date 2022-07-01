from datetime import datetime, date
import time
import tushare as ts


# timestamp--->datetime_str
def timeStamp2dateTime(time_Stamp):
    a = time.localtime(time_Stamp)
    b = time.strftime('%A %Y-%M-%d %H:%M:%S', a)
    return b


# datetime_str---->timestamp
def dateTime2timeStamp(datetime_str):
    return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')


def _random(n=13):
    from random import randint
    start = 10 ** (n - 1)
    end = (10 ** n) - 1
    return str(randint(start, end))


def get_today_ticks(str_code):
    df = ts.get_today_ticks(str_code)


# print(type(dateTime2timeStamp('2021-03-03 1:1:1')))
# print( _random())
get_today_ticks('000333')
