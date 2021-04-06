
import datetime
def get_day(day):
  l = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
  m,d,y = map(int,day.split('/'))
  return l[datetime.date(y,m,d).weekday()]

