
def first_tuesday_of_the_month(year, month): 
  from datetime import date as d
  day = 1
  while d(year, month, day).weekday() != 1:
    day += 1
  
  year, month, day = [str(item) for item in [year, month, day]]
  
  while len(month) < 2:
    month = '0' + month
  while len(day) < 2:
    day = '0' + day
  
  return '-'.join([year, month, day])

