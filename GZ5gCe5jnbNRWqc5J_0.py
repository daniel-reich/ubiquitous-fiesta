
from datetime import date
def first_tuesday_of_the_month(year, month):
  for day in range(1, 8):
    if date(year, month, day).weekday() == 1:
      return date(year, month, day).isoformat()

