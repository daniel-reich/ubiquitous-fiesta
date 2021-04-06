
def num_of_leapyears(years):
  def is_leap(year):
    if year % 4 != 0:
      return False
    elif year % 100 != 0:
      return True
    elif year % 400 != 0:
      return False
    return True
  start, end = [int(num) for num in years.split('-')]
  counter = 0
  cur_year = start
  while not is_leap(cur_year):
    cur_year += 1
  for year in range(cur_year, end + 1, 4):
    if is_leap(year):
      counter += 1
  return counter

