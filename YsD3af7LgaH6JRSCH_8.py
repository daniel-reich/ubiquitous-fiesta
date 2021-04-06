
from datetime import datetime as dt
from datetime import timedelta as td
def time_adjust(now, hrs=0, mins=0, sec=0):
  dt_now = dt.strptime(now, "%H:%M:%S")
  delta = td(hours=hrs, minutes=mins, seconds=sec)
  return dt.strftime(dt_now + delta, "%H:%M:%S")

