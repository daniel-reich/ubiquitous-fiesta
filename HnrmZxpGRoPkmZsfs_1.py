
import datetime
def is_valid_date(d, m, y):
  try:
    return bool(datetime.datetime(year= y, month=m, day= d))
  except:
    return False

