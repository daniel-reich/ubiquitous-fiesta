
from datetime import datetime,timedelta
def first_tuesday_of_the_month(year, month): 
  day = datetime(year,month,1)
  for i in range(7):
    if day.weekday()==1:
      return day.strftime('%Y-%m-%d')
    day+=timedelta(days=1)

