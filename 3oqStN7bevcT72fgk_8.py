
import datetime as dt
def get_day(d):
  m,d,y=map(int,d.split('/'))
  return dt.datetime(y,m,d).strftime('%A')

