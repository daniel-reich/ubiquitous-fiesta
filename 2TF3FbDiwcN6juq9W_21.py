
import datetime
def days_until_2021(date):
  parts = date.split('/')
  current = datetime.date(int(parts[2]),int(parts[0]),int(parts[1]))
  new_year = datetime.date(2021,1,1)
  delta = new_year - current
  return str(delta.days) + ' days' if delta.days > 1 else str(delta.days) + ' day'

