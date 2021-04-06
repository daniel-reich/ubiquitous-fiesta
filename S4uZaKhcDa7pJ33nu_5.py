
from datetime import timedelta
import datetime
def week_after(d):
  date = d.split("/")
  year = int(date[2])
  month = int(date[1])
  day = int(date[0])
  x = datetime.datetime(year, month, day)
  one_week = x + timedelta(days = 7)
  return one_week.strftime("%d"+"/""%m"+"/""%Y")

