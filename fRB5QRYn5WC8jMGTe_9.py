
from datetime import datetime,timedelta
def time_difference(city_a, timestamp, city_b):
  timestamp = datetime.strptime(timestamp,"%B %d, %Y %H:%M")
  cities = {'Los Angeles':-8,'New York':-5,'Caracas':-4.5,'Buenos Aires':-3,'London':0,'Rome':1,'Moscow':3,'Tehran':3.5,'New Delhi':5.5,'Beijing':8,'Canberra':10}
  diff = cities[city_b]-cities[city_a]
  timestamp += timedelta(hours=diff)
  return timestamp.strftime("%Y-%-m-%-d %H:%M")

