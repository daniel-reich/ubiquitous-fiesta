
import datetime
​
def is_valid_date(d, m, y):
  try:
    date = datetime.datetime(y, m, d)
  except ValueError:
    return False
  return True

