
import datetime
​
def get_days(date1, date2):
  delta = date2 - date1
  return round(delta.total_seconds() / 60 / 60 / 24)

