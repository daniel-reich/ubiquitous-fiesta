
import re
from datetime import datetime, timedelta
​
rx = re.compile(r'([a-z]+|\b\d{1,2}\b|\b\d{4}\b)', re.IGNORECASE)
dtformat = '%m %d %Y %H %M %z'
odtf = '{}-{}-{} {:02d}:{:02d}'
timezones = {
    'Los Angeles': '-0800', 
    'New York': '-0500',  
    'Caracas': '-0430', 
    'Buenos Aires': '-0300',  
    'London': '+0000',  
    'Rome': '+0100',  
    'Moscow': '+0300',  
    'Tehran': '+0330',  
    'New Delhi': '+0530', 
    'Beijing': '+0800', 
    'Canberra': '+1000' 
}
month = lambda s: str(('JanFebMarAprMayJunJulAugSepOctNovDec'.index(s[:3])) // 3 + 1).zfill(2)
​
def zonetime(city):
    tz = timezones[city]
    sign = -1 if tz[0] == '-' else 1
    return (sign * int(tz[1:3]), sign * int(tz[3:]))
​
def time_difference(city_a, timestamp, city_b):
    ca, cb = zonetime(city_a), zonetime(city_b)
    timediff = timedelta(hours=(cb[0] - ca[0]), minutes=(cb[1] - ca[1]))
    e = rx.findall(timestamp) + [timezones[city_a]]
    citya_datetime = datetime.strptime(month(e[0]) + ' ' + ' '.join(map(lambda s: s.zfill(2), e[1:])), dtformat)
    cityb_datetime = citya_datetime + timediff
    return odtf.format(cityb_datetime.year, cityb_datetime.month, cityb_datetime.day, cityb_datetime.hour, cityb_datetime.minute)

