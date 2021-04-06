
from datetime import datetime, timedelta
def time_difference(city_a, timestamp, city_b):
  tz = {'Los Angeles':-8,
    'New York':-5,
    'Caracas':-4.5,
    'Buenos Aires':-3,
    'London':0,
    'Rome':1,
    'Moscow':3,
    'Tehran':3.5,
    'New Delhi':5.5,
    'Beijing':8,
    'Canberra':10}
  
  time_difference = abs(tz[city_a]-tz[city_b])
  if tz[city_b] < tz[city_a]:
    time_difference *= -1
​
  new_time = datetime.strptime(timestamp,'%B %d, %Y %H:%M') + timedelta(hours=time_difference)
  return new_time.strftime('%Y-%m-%d %H:%M').replace('-0','-')

