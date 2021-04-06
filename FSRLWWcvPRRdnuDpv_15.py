
import math
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier
​
def mil_time_func(hour, AM_PM):
    if AM_PM == 'a.m.':
        hour = hour
    else:
        hour = hour + 12
    return hour
​
​
def min_in_decimals(minute):
    if minute == 0:
        minute_dec = 0
    else:
        minute_dec = minute / 60.0
    return minute_dec
​
​
def return_to_list_time(time):
    time_str = str(time)
    hour = int(time_str.split('.', 1)[0])
    minute = (time_str.split('.', 1)[1])
    if minute == 0:
        minute = 0
    else:
        minute_str = "0." + str(minute)
        minute_float = float(minute_str)
        minute = int(round_half_up(minute_float * 60))
    result = [hour, minute]
    return result
​
​
def time_to_eat(current_time):
    breakfast = 7.00
    lunch = 12.00
    dinner = 19.00
    hour = int(current_time.split(':', 1)[0])
    minute = int(current_time.split(':', 1)[1][0:2])
    AM_PM = current_time[-4:]
    mil_hour = mil_time_func(hour, AM_PM)
    minute_dec = min_in_decimals(minute)
    decimal_time = mil_hour + minute_dec
    if decimal_time < breakfast:
        decimal_time_to_eat = breakfast - decimal_time
    elif decimal_time < lunch:
        decimal_time_to_eat = lunch - decimal_time
    elif decimal_time < dinner:
        decimal_time_to_eat = dinner - decimal_time
    else:
        decimal_time_to_eat = 31.00 - decimal_time
    result = return_to_list_time(decimal_time_to_eat)
    return result

