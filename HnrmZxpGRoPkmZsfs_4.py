
import datetime
def is_valid_date(d, m, y):
  valid = True
  try:
    datetime.datetime(y,m,d)
  except ValueError:
    valid = False
  return valid

