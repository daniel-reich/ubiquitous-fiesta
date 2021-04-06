
from datetime import datetime
from time import strptime
from datetime import timedelta
def time_difference(city_a, timestamp, city_b):
    dic = {"Los Angeles": -8, "New York": -5, "Caracas": -4.5, "Buenos Aires": -3, "London": 0, "Rome": 1, "Moscow": 3, "Tehran": 3.5, "New Delhi": 5.5, "Beijing": 8, "Canberra": 10}
    t = (abs(dic.get(city_a) - dic.get(city_b)))
    if (dic.get(city_a) > dic.get(city_b)):
        t = t * -1
    date_z = datetime.strptime(timestamp, ("%B %d, %Y %H:%M"))
    date_r = date_z + timedelta(hours = t)
    return(str(date_r.strftime("%Y-%-m-%-d %H:%M")))

