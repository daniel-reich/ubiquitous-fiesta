
import calendar
def has_friday_13(month, year):
   return calendar.monthrange(year, month)[0] == 6

