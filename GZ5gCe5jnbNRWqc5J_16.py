
import datetime
​
def first_tuesday_of_the_month(year, month): 
  for i in range(1, 8):
    if datetime.datetime(year, month, i).weekday() == 1:
      if month < 10:
        month = '0'+str(month)
      else:
        month = str(month)
      i = '0' + str(i)
      return str(year) + "-" + month + "-" + i

