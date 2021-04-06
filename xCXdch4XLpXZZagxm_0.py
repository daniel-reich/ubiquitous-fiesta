
from calendar import isleap
​
def num_of_leapyears(years):
  start, end = map(int, years.split('-'))
  return sum(isleap(year) for year in range(start, end+1))

