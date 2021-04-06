
def get_day(day):
  from datetime import datetime as dt
  a = [int(i) for i in day.split("/")]
  return dt(a[2],a[0],a[1]).strftime('%A')

