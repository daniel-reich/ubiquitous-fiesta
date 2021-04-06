
def is_leap(year):
  if (not year % 400) or (year % 100 and not year % 4):
    return True
  return False
​
def num_of_leapyears(years):
  start, end = [int(i) for i in years.split('-')]
  return sum(1 for y in range(start, end + 1) if is_leap(y))

