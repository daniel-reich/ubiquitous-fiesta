
from datetime import date, timedelta
​
​
def week_after(d):
  day, month, year = map(int, d.split('/'))
  week = date(year, month, day) + timedelta(days=7)
  return '{:02d}/{:02d}/{}'.format(week.day, week.month, week.year)

