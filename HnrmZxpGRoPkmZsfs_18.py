
import datetime
def is_valid_date(d, m, y):
  try:
    date = datetime.datetime(int(y), int(m), int(d))
    return True
  except:
    return False

