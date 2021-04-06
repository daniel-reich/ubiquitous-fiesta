
import datetime
def get_day(day):
  m,d,y = day.split('/')
  date = datetime.datetime(int(y),int(m),int(d))
  return date.strftime("%A")

