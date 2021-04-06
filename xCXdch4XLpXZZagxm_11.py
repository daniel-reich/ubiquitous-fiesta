
from calendar import isleap
​
​
def num_of_leapyears(years):
  start, stop = (int(i) for i in years.split('-'))
  return sum(isleap(i) for i in range(start, stop + 1))

