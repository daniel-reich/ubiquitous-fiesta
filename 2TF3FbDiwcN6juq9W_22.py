
from datetime import datetime
​
def days_until_2021(date):
  month, day, _ = map(int, date.split('/'))
  days = (datetime(2021, 1, 1) - 
    datetime(2020, month, day)).days
  return str(days) + ' day' + 's' * (days > 1)

