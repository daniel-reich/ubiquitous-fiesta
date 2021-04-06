
from datetime import datetime as t
def is_valid_date(d, m, y):
  try:
    if t(y,m,d):
      return True
  except:
    return False

