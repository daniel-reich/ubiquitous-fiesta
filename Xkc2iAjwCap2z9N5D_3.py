
import datetime
def has_friday_13(month, year):
  isFriday = False
  defineDay = datetime.datetime(year, month, 13)
  weekdayOf13th = defineDay.strftime("%A")
  if weekdayOf13th == str("Friday"):
    isFriday = True
  return(isFriday)

