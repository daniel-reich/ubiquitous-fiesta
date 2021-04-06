
import datetime
def get_day(day):
  y = int(day.split("/")[len(day.split("/"))-1])
  d = int(day.split("/")[1])
  m = int(day.split("/")[0])
  return datetime.datetime(y, m, d).strftime("%A")

