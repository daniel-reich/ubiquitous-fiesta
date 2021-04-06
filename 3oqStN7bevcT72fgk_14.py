
import datetime
import calendar
​
def get_day(d):
    month , day , year  = (int(e)  for e in d.split("/"));
    today =  datetime.datetime(year, month, day).weekday();
    return calendar.day_name[today];

