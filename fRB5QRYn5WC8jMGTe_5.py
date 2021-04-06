
from datetime import datetime, timedelta
​
​
def time_difference(city_a, timestamp, city_b):
    dict = {"Los Angeles": -8, 'New York': -5, 'Caracas': -4.5, 'Buenos Aires': -3, 'London': 0, 'Rome': 1,'Moscow': 3, 'Tehran': 3.5, 'New Delhi': 5.5, 'Canberra': 10, 'Beijing': 8 }
    a = dict[city_a]
    b = dict[city_b]
    if int(b - a) != b - a and b - a > 0:
        m = 30
        h = 0
    elif int(b - a) != b - a and b - a < 0:
        m = 30
        h = -1
    else:
        m = 0
        h = 0
    newTime = datetime.strptime(timestamp, '%B %d, %Y %H:%M') + timedelta(hours = int(b - a + h), minutes = m)
    return newTime.strftime('%Y-%m-%d %H:%M').replace('-0', '-')

