
import datetime
def is_valid_date(d, m, y):
  is_valid_date = True
  try: datetime.datetime(y, m, d)
  except ValueError: is_valid_date = False
  return is_valid_date

