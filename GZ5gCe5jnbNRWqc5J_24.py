
from datetime import datetime
​
def first_tuesday_of_the_month(year, month): 
  day = datetime(year, month, 1).weekday()
  key = {2:7, 0:2, 6:3, 5:4, 4:5, 1:1, 3:6}
  return '{}-{:02}-{:02}'.format(year, month, key[day])

