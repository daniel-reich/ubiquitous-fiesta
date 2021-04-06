
def num_of_leapyears(years):
  start,end = map(int,years.split('-'))
  return sum(not y%400 or (y%100 and not y%4) for y in range(start,end+1))

