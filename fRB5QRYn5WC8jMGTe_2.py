
from datetime import *
from dateutil.parser import *
def time_difference(city_a, timestamp, city_b):
  GMT = {'Los Angeles':-8, 'New York':-5, 'Caracas':-4.5, 'Buenos Aires':-3, 'London':0, 
  'Rome':1, 'Moscow':3, 'Tehran':3.5, 'New Delhi':5.5, 'Beijing':8,
  'Canberra':10}
  
  ta = timedelta(hours = GMT[city_a])
  tb = timedelta(hours = GMT[city_b])
  date = parse(timestamp) + (tb - ta)
  return date.strftime("%Y-%m-%d %H:%M").replace('-0','-')

