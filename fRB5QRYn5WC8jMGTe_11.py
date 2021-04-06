
from datetime import timedelta
from datetime import datetime as dt
def time_difference(city_a, timestamp, city_b):
    city={
        "Los Angeles": -8,
        "New York": -5,
        "Caracas": -4.5,
        "Buenos Aires": -3,
        "London": 0,
        "Rome": 1,
        "Moscow": 3,
        "Tehran": 3.5,
        "New Delhi": 5.5,
        "Beijing": 8,
        "Canberra": 10
    }
    newtime=dt.strptime(timestamp,"%B %d, %Y %H:%M")+timedelta(hours=city[city_b]-city[city_a])
    s=newtime.strftime("%Y-%m-%d %H:%M")
    f=1
    if s[5]=='0':
        s=s[:5]+s[6:]
        f=0
    if s[7+f]=='0':
        s=s[:7+f]+s[8+f:]
    return s

