
import datetime
def has_friday_13(month, year):
  T = datetime.datetime(year,month,13)
  return T.strftime("%A") == "Friday"

