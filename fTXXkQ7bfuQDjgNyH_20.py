
from datetime import date
def day_of_year(date_str):
  m,d,y = [int(itm) for itm in date_str.split('/')]
  t1 = date(y, m, d).toordinal()
  t0 = date(y, 1, 1).toordinal()
  return t1 - t0 + 1

