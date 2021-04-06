
import calendar
def num_of_leapyears(years):
  y = list(map(int,years.split("-")))
  k = 0
  
  for i in range(y[0],y[1]+1, 1):
    if (calendar.isleap(i)):
      k += 1
  return k

