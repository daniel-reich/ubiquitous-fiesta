
import datetime
​
def has_friday_13(month, year):
  dato = datetime.datetime(year, month, 13)
  if dato.weekday() == 4:
    return True
  return False

