
import calendar
​
def num_of_leapyears(years):
  r = [int(x) for x in years.split('-')]
  return [calendar.isleap(int(y)) for y in range(r[0], r[1] + 1)].count(True)

