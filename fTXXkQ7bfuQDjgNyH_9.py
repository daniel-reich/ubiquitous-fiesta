
from datetime import datetime as dt, timedelta as td, time as t
def day_of_year(date):
  s=date.split('/')
  d1=dt.strptime(date, '%m/%d/%Y')
  d2=dt.strptime('1/'+'1/'+s[-1], '%m/%d/%Y')
  return (d1-d2).days+1

