
import datetime
def get_day(day):
  m,d,y = [int(i) for i in day.split('/')]
  days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
  return days[datetime.date(y,m,d).weekday()]

