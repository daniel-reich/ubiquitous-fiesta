
import datetime
def is_valid_date(d, m, y):
  try:
    datetime.date(y, m, d)
    return True
  except:
    return False

