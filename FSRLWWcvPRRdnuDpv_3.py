
import re
import datetime
​
def time_to_eat(current_time):
  current_time = re.sub('\.', '', current_time).upper()
  dt = datetime.datetime.strptime(current_time, '%I:%M %p')
  hour = dt.hour + dt.minute/60
  if (hour <= 7):
    result = 7 - hour
  elif (hour <= 12):
    result =  12 - hour
  elif (hour <= 19):
    result =  19 - hour
  else:
    result =  24 - hour + 7
  return [int(result), round(60*(result-int(result)))]

