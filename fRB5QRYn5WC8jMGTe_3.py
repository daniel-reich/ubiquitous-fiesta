
from dateutil.parser import parse
from datetime import datetime as dt, timedelta as td
​
def time_difference(city_a, timestamp, city_b):
  d = {
    'Los Angeles': -8, 'New York': -5, 'Caracas': -4.5,
      'Buenos Aires': -3, 'London': 0, 'Rome': 1,
    'Moscow': 3, 'Tehran': 3.5, 'New Delhi': 5.5,
    'Beijing': 8, 'Canberra': 10
    }
  time = parse(timestamp) - td(hours=d[city_a]) + td(hours=d[city_b])
  return dt.strftime(time, '%Y-%-m-%-d %H:%M')

