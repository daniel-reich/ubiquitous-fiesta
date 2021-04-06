
from datetime import datetime, timedelta
def time_difference(city_a, timestamp, city_b):
  dic = {
  'Los Angeles':-8,
  'New York':-5,
  'Caracas':-4.5,
  'Buenos Aires':-3,
  'London':0,
  'Rome':1,
  'Moscow':3,
  'Tehran':3.5,
  'New Delhi':5.5,
  'Beijing':8,
  'Canberra':10
  }
  now = datetime.strptime(timestamp, '%B %d, %Y %H:%M')
  difference = dic[city_b] - dic[city_a]
  new = now + timedelta(hours=difference)
  return new.strftime('%Y-%-m-%-d %H:%M')

