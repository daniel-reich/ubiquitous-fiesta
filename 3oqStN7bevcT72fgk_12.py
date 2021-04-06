
from datetime import date
​
def get_day(day):
  m, d, y = map(int, day.split('/'))
  return date(y, m, d).strftime('%A')

