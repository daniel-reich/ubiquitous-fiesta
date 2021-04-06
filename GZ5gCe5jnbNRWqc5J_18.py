
from datetime import datetime
def first_tuesday_of_the_month(year, month): 
  for i in range(1,8):
    day = datetime(year,month,i)
    if day.weekday() == 1:
      return datetime.strftime(day,'%Y-%m-%d')

