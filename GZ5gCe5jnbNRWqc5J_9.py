
import datetime as dt
​
def first_tuesday_of_the_month(year, month):
    day = ['02', '01', '07', '06', '05', '04', '03']  
    d = dt.datetime(year, month, 1)
    dd = day[d.weekday()]
    mm = str(month).zfill(2)
    return str(year) + '-' + mm + '-' + dd

