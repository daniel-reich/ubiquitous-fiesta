
import calendar as c
def get_day(day):
  m, d, y = int(day[:2]), int(day[3:5]), int(day[6:])
  wd = c.weekday(y,m,d)
  return c.day_name[wd]

