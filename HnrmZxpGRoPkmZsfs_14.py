
import datetime
def is_valid_date(d, m, y):
  try:
    date = datetime.date(y,m,d)
    return True
  except:
    return False

