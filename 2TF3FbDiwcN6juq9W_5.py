
from datetime import datetime
​
def days_until_2021(date):
  day=(datetime(2021,1,1)-datetime.strptime(date, '%m/%d/%Y')).days
  if day>1:
    return '{} days'.format(day)
  return  '{} day'.format(day)

