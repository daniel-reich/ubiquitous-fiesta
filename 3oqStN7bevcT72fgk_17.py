
from datetime import date
​
def get_day(day):
  days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  day = day.split('/')
  dow = date(int(day[2]), int(day[0]), int(day[1])).weekday()
  return days[dow]

