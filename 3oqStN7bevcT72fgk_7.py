
import datetime as dt
​
def get_day(day):
    """MM/DD/YYYY"""
    weekdays = {7:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
    lst = [int(x) for x in day.split('/')]
    d = dt.date(lst[2], lst[0], lst[1]) # "YYYY,MM,DD"
    return weekdays[d.isoweekday()]

