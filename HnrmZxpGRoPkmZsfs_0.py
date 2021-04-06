
from datetime import date
​
def is_valid_date(d, m, y):
  try: d = date(y, m, d)
  except: return False
  return True

