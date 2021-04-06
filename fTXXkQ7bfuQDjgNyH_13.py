
from datetime import datetime
​
def day_of_year(date):
  d1 = datetime(int(date[-4:]), 1, 1)
  d2 = datetime.strptime(date, '%m/%d/%Y')
  return (d2 - d1).days + 1

