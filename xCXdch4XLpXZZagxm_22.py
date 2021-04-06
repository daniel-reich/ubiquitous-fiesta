
import calendar
def num_of_leapyears(years):
  s = 0
  for i in range(int(years.split('-')[0]),int(years.split('-')[1])+1):
    if calendar.isleap(i):
      s += 1
  return s

