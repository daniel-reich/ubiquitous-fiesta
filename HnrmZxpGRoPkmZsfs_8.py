
import datetime
def is_valid_date(d, m, y):
  try:
    x = datetime.datetime(y,m,d)
    return True
  except:
    return False

