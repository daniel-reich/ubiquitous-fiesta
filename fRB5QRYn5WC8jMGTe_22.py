
from datetime import datetime, timedelta
time_zones = {'Los Angeles':(-8, 0), 'New York':(-5, 0), 'Caracas':(-4, -30),
  'Buenos Aires':(-3, 0), 'London':(0, 0), 'Rome':(1, 0), 'Moscow':(3, 0),
  'Tehran':(3, 30), 'New Delhi':(5, 30), 'Beijing':(8, 0), 'Canberra':(10, 0)}
def time_difference(city_a, timestamp, city_b):
  time = datetime.strptime(timestamp, "%B %d, %Y %H:%M")
  da = timedelta(hours=time_zones[city_a][0], minutes=time_zones[city_a][1])
  db = timedelta(hours=time_zones[city_b][0], minutes=time_zones[city_b][1])
  return (time - da + db).strftime("%Y-%-m-%-d %H:%M")

