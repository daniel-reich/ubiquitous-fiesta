
from datetime import datetime, timedelta
d={'Los Angeles':timedelta(hours=-8),'New York':timedelta(hours=-5),\
  'Caracas':timedelta(minutes=-30, hours=-4),'Buenos Aires':timedelta(hours=-3),\
  'London':timedelta(hours=0),'Rome':timedelta(hours=1),'Moscow':timedelta(hours=3),\
  'Tehran':timedelta(minutes=30, hours=3),'New Delhi':timedelta(minutes=30, hours=5),\
  'Beijing':timedelta(hours=8),'Canberra':timedelta(hours=10)}
def time_difference(city_a, timestamp, city_b):
  return (datetime.strptime(timestamp,'%B %d, %Y %H:%M')+d[city_b]-d[city_a]).strftime('%Y-%-m-%-d %H:%M')

