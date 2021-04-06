
import datetime
​
def first_tuesday_of_the_month(year, month): 
  d = datetime.datetime(year, month, 1).weekday()
  
  if d == 0:
    sol = 2
  elif d == 1:
    sol = 1
  else:
    sol = (1 - d) + 8
  
  return '{}-{:02d}-{:02d}'.format(year, month, sol)

