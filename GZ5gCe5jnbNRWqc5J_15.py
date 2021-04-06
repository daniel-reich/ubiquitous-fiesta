
from datetime import datetime
​
def first_tuesday_of_the_month(year, month): 
  for day in range(1, 8):
    date = (year, month, day)
    
    if datetime(*date).strftime('%a') == 'Tue':
      return '{}-{:02}-{:02}'.format(*date)

