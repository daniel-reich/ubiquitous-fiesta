
from calendar import isleap
​
def num_of_leapyears(years):
  y1, y2 = map(int, years.split('-'))
  return sum(isleap(y) for y in range(y1, y2 + 1))

