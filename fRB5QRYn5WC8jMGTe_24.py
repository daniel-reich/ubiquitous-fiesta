
import re
from datetime import datetime, timedelta
​
def time_difference(a, t, b):
  timess = {
  'Los Angeles' : -8  , 'New York': -5  , 'Caracas' : -4.5  ,
  'Buenos Aires'  : -3  , 'London'  : 0   , 'Rome'  : 1     ,
  'Moscow'    : 3   , 'Tehran'  : 3.5 , 'New Delhi': 5.5  , 
  'Beijing'   : 8   , 'Canberra': 10  }
  
  return re.sub('-0', '-', (datetime.strptime(t, '%B %d, %Y %H:%M') \
  + timedelta(hours = timess[b]-timess[a])).strftime('%Y-%m-%d %H:%M'))

