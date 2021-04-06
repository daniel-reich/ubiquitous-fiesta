
import datetime
def get_day(day):
  date = day.split('/')
  m = int(date[0])
  d = int(date[1])
  y = int(date[2])
  return datetime.date(y,m,d).strftime("%A")

