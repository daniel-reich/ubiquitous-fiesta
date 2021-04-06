
from datetime import timedelta, datetime
​
def week_after(date):
  d, m, y = [int(x) for x in date.split('/')]
  return (datetime(y, m, d) + timedelta(7)).strftime('%d/%m/%Y')

