
import datetime
def is_valid_date(d, m, y):
  try:
    datetime.datetime(y, m, d)
    return True
  except ValueError:
    return False

