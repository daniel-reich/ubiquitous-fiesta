
import datetime
def has_friday_13(month, year):
  ans = datetime.datetime(year, month, 13)
  Weekday = ans.strftime("%A")
  Day_of_Month = ans.strftime("%d")
  if Weekday == "Friday" and Day_of_Month == "13":
    return True
  return False

