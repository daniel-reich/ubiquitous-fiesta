
import calendar
def has_friday_13(month, year):
  return calendar.weekday(year, month, 13) == 4

