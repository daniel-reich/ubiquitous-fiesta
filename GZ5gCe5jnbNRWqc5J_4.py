
import datetime
def first_tuesday_of_the_month(year, month): 
  day = 1
  while datetime.datetime(year,month,day).strftime('%A') != 'Tuesday':
    day += 1
  else:
    return datetime.datetime(year,month,day).strftime('%Y-%m-%d')

