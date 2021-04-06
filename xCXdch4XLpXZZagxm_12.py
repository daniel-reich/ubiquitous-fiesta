
import calendar
def num_of_leapyears(years):
  low = int(years.split("-")[0])
  high  = int(years.split("-")[1])
  count = 0
  for i in range(low, high+1):
    if calendar.isleap(i):
      count+=1
  
  return count

