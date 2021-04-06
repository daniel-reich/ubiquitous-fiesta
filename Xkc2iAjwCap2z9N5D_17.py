
import calendar
def has_friday_13(month, year):
  if calendar.weekday(year, month, 13) == 4:
    return True
  else:
    return False

