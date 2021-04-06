
from datetime import datetime, timedelta
​
tz = {"Los Angeles": "-08:00", "New York": "-05:00", "Caracas": "-05:30",
         "Buenos Aires": "-03:00", "London": "00:00", "Rome": "+01:00",
         "Moscow": "+03:00", "Tehran": "+03:30", "New Delhi": "+05:30",
         "Beijing": "+08:00", "Canberra": "+10:00"}
​
def time_difference(city_a, timestamp, city_b):
  dt = datetime.strptime(timestamp, "%B %d, %Y %H:%M")
  # city_a time taken to UTC:
  delta_a = timedelta(hours = int(tz[city_a][:-3]), minutes = int(tz[city_a][-2:]))
  # city_b time taken to UTC:
  delta_b = timedelta(hours = int(tz[city_b][:-3]), minutes = int(tz[city_b][-2:]))
  new_dt = dt - delta_a + delta_b
  return new_dt.strftime("%Y-%-m-%-d %H:%M")

