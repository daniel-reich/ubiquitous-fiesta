
import datetime
​
def has_friday_13(month, year):
  if(datetime.date(year, month, 13).weekday() == 4):
    return True
  else:
    return False

