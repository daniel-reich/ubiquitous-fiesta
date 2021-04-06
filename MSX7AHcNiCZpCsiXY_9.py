
from datetime import date, timedelta
def how_unlucky(y):
  d1 = date(y,1,1)
  d2 = date(y,12,31)
  return sum([True for x in range((d2-d1).days+1) if (d1+timedelta(days=x)).weekday() == 4 and (d1+timedelta(days=x)).day==13])

