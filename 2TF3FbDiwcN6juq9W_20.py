
from datetime import datetime, date, timedelta
​
def days_until_2021(t1):
  a = "days"
  t1 = datetime.strptime(t1, '%m/%d/%Y')
  t2 = datetime(2021, 1, 1)
  if (t2-t1).days == 1:
    a = "day"
  return '{} {}'.format((t2-t1).days, a)

