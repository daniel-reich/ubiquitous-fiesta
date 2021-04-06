
from datetime import date
def has_friday_13(month, year):
  if date(year, month, 13).isoweekday() == 5:
    return True
  return False

