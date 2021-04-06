
def num_of_leapyears(years):
  x = years.split("-")
  def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
  count  = 0
  for year in range(int(x[0]),int(x[1])+1):
    if is_leap_year(year):
      count+= 1
  return count

