
import calendar
def num_of_leapyears(years):
  x = years.split('-')
  first_year = int(x[0])
  second_year = int(x[1])
  count = 0
  for i in range(first_year,second_year+1):
    if calendar.isleap(i):
      count += 1
  return count

