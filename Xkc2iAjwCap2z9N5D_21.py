
import datetime
​
def has_friday_13(month, year):
  return datetime.date(day = 13, month = month, year = year).weekday()==4

