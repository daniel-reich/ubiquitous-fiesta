
import datetime
def get_day(day):
  m,d,y=map(int,day.split("/"))
  return datetime.datetime(y, m, d).strftime("%A")

